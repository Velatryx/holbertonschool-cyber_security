#!/bin/bash
snmpwalk -v 2c -c public "$1" 2>/dev/null | grep "sysDescr" && grep -i "public" /etc/snmp/snmpd.conf 2>/dev/null
