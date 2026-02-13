#!/bin/bash
snmpwalk -v 2c -c public "$1" 2>/dev/null | grep "sysDescr"
