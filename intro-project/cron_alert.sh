#!/bin/bash

data=$(cut -d "," -f 2 fatal.csv | sort | uniq -c)


error=$(echo "$data" | cut -d " " -f 1)
fatal=$(echo "$data" | cut -d " " -f 3)


if [ "$error" -ge 5 ] || [ "$fatal" -ge 1 ]; then 
    echo "$(date): System needs attention" > fatal_error.txt
fi