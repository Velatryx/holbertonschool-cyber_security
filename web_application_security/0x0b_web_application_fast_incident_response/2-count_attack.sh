#!/bin/bash

file=logs.txt

awk '{print $1}' $file | sort | uniq -c | sort -rn | head -1 | awk '{print $1}'
