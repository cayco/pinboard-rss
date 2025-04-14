#!/bin/bash
#

cd /home/cayco/pinboard-rss/pinboard-rss-gha
source .env
python3 run.py > rss/pinboard.xml
npx wrangler pages deploy ./rss --project-name pinboard-popular --commit-dirty=true
