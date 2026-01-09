#!/bin/bash
sudo nmap -sn -UP22,80,443 $1
