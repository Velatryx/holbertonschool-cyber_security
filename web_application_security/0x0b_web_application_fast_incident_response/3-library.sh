#!/bin/bash

file=logs.txt

awk '{print $12}' $file | sort | uniq -c | sort -rn | head -1 | tr -d '"' | awk '{print $2}' 
