#!/bin/bash
sudo nmap -PS20,80,443 -sn $1
