#!/bin/bash
postconf smtconf smtpd_tls_security_level | grep -q "^smtpd_tls_security_level = \(may\|encrypt\)"
