#!/bin/bash

data=$(cut -d ',' -f 1 product.csv | sort | uniq -c)

unique_value=$(echo "$data" | cut -d ' ' -f 1)

for value in $unique_value; do
    if [ "$value" -gt 1 ]; then
        echo "duplicate values in file: $value"
    fi
done