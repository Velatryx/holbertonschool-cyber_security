#!/bin/bash

file=$1

awk '{print $6}' $file | sort | uniq -c | sort -rn
