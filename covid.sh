#!/bin/bash
# This script downloads covid data and displays it
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
TOTALTESTRESULTS=$(echo $DATA | jq '.[0].totalTestResults')
DEATH=$(echo $DATA | jq '.[0].death')

TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative COVID cases, $DEATH deathes, and $TOTALTESTRESULTS total test results"

