#!/bin/bash

file=logs.txt
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" "$file" | sort | uniq -c | sort -rn | head -1 | awk '{print $2}'
