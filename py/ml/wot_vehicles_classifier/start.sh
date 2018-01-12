#!/bin/bash

printf "WoT Classifier\n"
printf "Fetching vehicles list...\n"
python3.6 fetcher.py
printf "Processing vehicles...\n"
python3.6 processor.py
printf "Splitting train data...\n"
python3.6 split.py
printf "Starting classifier...\n\n"
python3.6 index.py
