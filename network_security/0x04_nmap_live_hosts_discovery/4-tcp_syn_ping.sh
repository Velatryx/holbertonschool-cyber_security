#!/bin/bash
sudo nmap -p20,80,443 -sn -sS $1
