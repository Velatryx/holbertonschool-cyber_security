#!/bin/bash
BEGIN {
  ORS=""
  cmd="whois " ARGV[1]
  first=1
  while ((cmd | getline line) > 0)
    if (line ~ /^(Registrant|Admin|Tech)/) {
      split(line,a,":")
      v=a[2]; sub(/^ /,"",v)
      if (a[1] ~ /Street$/) v=v" "
      if (a[1] ~ /Ext$/) a[1]=a[1]":"
      if (!first) print "\n"
      first=0
      print a[1] "," v
    }
  close(cmd)
}

