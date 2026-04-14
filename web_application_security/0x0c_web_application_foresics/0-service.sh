#!/bin/bash

file=$1

awk '{print $5}' $file | sort | uniq -c | sort -rn
