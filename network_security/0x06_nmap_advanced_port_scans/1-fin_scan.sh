#!/bin/bash
sudo nmap $1 -sF -f -t 2 -p80-85
