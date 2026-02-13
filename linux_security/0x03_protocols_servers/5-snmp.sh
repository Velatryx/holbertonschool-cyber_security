#!/bin/bash
snmpwalk -c public "$1" 2>/dev/null
