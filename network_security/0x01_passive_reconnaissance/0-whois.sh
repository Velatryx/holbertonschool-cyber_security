#!/bin/bash
whois "$1" | awk 'BEGIN{ORS=""}/^(Registrant|Admin|Tech)/{sub(/^ /,"",$0);split($0,a,":");if(a[1]~/Ext$/)a[1]=a[1]":";v=a[2];sub(/[[:space:]]+$/,"",v);if(v=="")v=" ";print(n++?"\n":"") a[1] ", " v}' > "$1".csv
