#!/bin/bash
sudo nmap -sM -p http*, ftp, ssh, telnet $1 -vv
