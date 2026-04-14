#!/bin/bash

file=$1

awk '{count[$6]++} END {for (service in count) print count[service], service}' $file | sort -rn
