# Pinboard public RSS

This would run, generate and publish to Cloudflare Pages rss file from [pinboard.in/public](https://pinboard.in/popular/) page.

## Setting up

* set up your Cloudflare Pages
* create .env file in the cloned repo containing CLOUDFLARE_ACCOUNT_ID and CLOUDFLARE_API_TOKEN - generated in the previous step
* run ./publish.sh manually to confirm your wrangler works and you have all Python deps installed
* set up publish.sh to be run by cron in /etc/crontab: `45 *	* * *	root	cd /home/user/pinboard-rss && ./publish.sh`
