#!/bin/bash

while IFS= read -r line; do
    echo "$line" | python3 cw_weight.py
done
