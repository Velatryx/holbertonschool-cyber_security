#!/bin/bash
subfinder -d "$1" -silent | while read host; do ip=$(dig +short "$host" | head -n1); echo "$host,$ip"; done > "$1".txt
