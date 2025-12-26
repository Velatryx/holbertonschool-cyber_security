#!/bin/bash
whois "$1" | awk 'BEGIN{ORS=""}/^(Registrant|Admin|Tech)/{split($0,a,":");v=a[2];sub(/^ /,"",v);if(a[1]~/Ext$/&&v=="")v=" ";if(v=="")v=" ";print(n++?"\n":"") a[1] ", " v}' > "$1".csv
