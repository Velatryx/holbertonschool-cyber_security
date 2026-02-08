#!/bin/bash
echo -n "$1" | openssl sha256 | awk '{print $2}' 1>3_hash.txt
