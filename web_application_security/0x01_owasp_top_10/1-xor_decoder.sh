#!/usr/bin/env bash
# Accept hash as argument
encoded="$1"

# Remove {xor} tag if present
encoded="${encoded#\{xor\}}"

# Decode and XOR 0x5F
decoded=$(echo "$encoded" | base64 --decode 2>/dev/null | \
  perl -ne 'foreach $c (split //) { printf "%s", chr(ord($c) ^ 0x5f) }')

echo "$decoded"
