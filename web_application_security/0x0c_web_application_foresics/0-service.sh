#!/bin/bash

awk '{print $5}' auth.log | cut -d'[' -f1 | sort | uniq -c | sort -nr
