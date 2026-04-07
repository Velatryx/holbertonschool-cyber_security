#!/bin/bash

file=logs.txt
awk '{print $7}' "$file" | sort | uniq -c | sort -r | head -1 | awk '{print $2}'
