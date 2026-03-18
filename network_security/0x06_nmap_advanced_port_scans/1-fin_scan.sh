#!/bin/bash
sudo nmap $1 -sF -f --timing 2 -p80-85
