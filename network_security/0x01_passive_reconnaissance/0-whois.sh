#!/bin/bash
whois "$1" | awk 'BEGIN{ORS=""}/^(Registrant|Admin|Tech)/{split($0,a,":");v=a[2];sub(/^ /,"",v);if(a[1]~/Ext$/) a[1]=a[1]":";if(v=="")v=" ";v=gensub(/[[:space:]]+$/,"","g",v);print(n++?"\n":"") a[1] ", " v}' > "$1".csv
