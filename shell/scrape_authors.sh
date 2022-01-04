#!/bin/bash

# This is meant to run as a cronjob.
# Example cronjob format (runs every Friday at 19:00):
# 00 19 * * 5 /path/to/astroph-coffee/shell/scrape_authors.sh \
# /path/to/astroph-coffee > \
# /path/to/astroph-coffee/run/logs/author-auto-update.log 2>&1


if [ $# -lt 1 ]
then
    echo "Usage: $0 <astroph-coffee basepath>"
    exit 2
fi


BASEPATH=$1

echo "arxiv update started at:" `date`
echo "astro-coffee server directory: $BASEPATH"

cd $BASEPATH/run
source $BASEPATH/run/bin/activate

python $BASEPATH/run/scrape_authors.py $BASEPATH/run/static/images/AstroDeptList.csv

deactivate

echo "local author update ended at: " `date`
cd -