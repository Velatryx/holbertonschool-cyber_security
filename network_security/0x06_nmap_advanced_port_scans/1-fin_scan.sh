#!/bin/bash
sudo nmap $1 -sF -f -T2 -p80-85
