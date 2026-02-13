#!/bin/bash
postconf smtpd_tls_security_level | grep -qE "may|encrypt"
