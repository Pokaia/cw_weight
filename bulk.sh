#!/bin/bash

while IFS= read -r line; do
	echo -n "$line: "
    echo "$line" | python3 cw_weight.py
done
