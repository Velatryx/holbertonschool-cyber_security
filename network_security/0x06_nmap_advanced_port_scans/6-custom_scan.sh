#!/bin/bash
sudo nmap --scanflags URGACKPSHRSTSYNFINECECWR $1 -p $2 -oN custom_scan.txt 2>&1 /dev/null
