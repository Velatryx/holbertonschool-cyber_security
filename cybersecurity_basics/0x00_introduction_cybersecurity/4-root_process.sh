#!/bin/bash
ps aux | grep -i "^$1" | grep -vE '0 +0 '
