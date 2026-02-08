#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt "$1" && john --show --format=Raw-SHA256 "$1" | awk -F: '{print $2}' > 6-password.txt
