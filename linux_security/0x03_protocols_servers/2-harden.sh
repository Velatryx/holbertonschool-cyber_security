#!/bin/bash
find /home /var -xdev -type d -perm -0002 -exec chmod o-w {} +
