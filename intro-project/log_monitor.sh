#!/bin/bash

# Need to install inotify-tools on linux

FILE='./fatal.csv'

file1=/var/log/app.log

while true; do

    inotifywait -e modify /var/log/app.log

    data=$(tail -n 1 "$file1" | sed 's/\[/,/g' | sed 's/\]/,/g')

    error=$(echo "$data" | cut -d ',' -f 2)
    if [ "$error" == 'ERROR' ] || [ "$error" == 'FATAL' ]; then
        echo "$data" >> $FILE 
    fi
    
done