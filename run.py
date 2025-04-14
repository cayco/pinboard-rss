import datetime as dt
from bs4 import BeautifulSoup
import requests
from textwrap import dedent
import xml.sax.saxutils

URL = "https://www.pinboard.in/popular/"


def get_html() -> str:
    r = requests.get(URL)
    r.raise_for_status()
    return r.text


def process_link(title: str, link: str) -> str:
    safe_title = xml.sax.saxutils.escape(title)
    safe_link = xml.sax.saxutils.escape(link)
    return f"<item><title>{safe_title}</title><link>{safe_link}</link><guid>{safe_link}</guid></item>"

def generate_feed() -> str:
    soup = BeautifulSoup(get_html(), "html.parser")
    links = "\n\t\t\t".join([
        process_link(link.text, link["href"])
        for link in soup.find_all("a", "bookmark_title")
    ])
    
    return dedent(f"""\
    <rss version="2.0">
        <channel>
            <title>Pinboard Popular</title>
            <link>{URL}</link>
            <description>Pinboard popular</description>
            {links}
        </channel>
    </rss>
    """)


if __name__ == "__main__":
    print(generate_feed())
