#!/bin/bash
sudo nmap --scanflags URGACKPSHRSTSYNFINECECWR $1 -p $2 -oN custom_scan.txt > /dev/null 2>&1
