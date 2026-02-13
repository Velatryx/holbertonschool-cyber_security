#!/bin/bash
nmap -sV --script ssl-enum-ciphers -p 443 <target_ip>
