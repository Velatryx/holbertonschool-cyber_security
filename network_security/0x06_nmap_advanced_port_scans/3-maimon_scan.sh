#!/bin/bash
sudo nmap -sM -p http, https, ftp, ssh, telnet $1 -vv
