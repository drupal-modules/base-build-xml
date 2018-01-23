#!/usr/bin/env bash
[ $# -eq 0 ] && { echo "Usage: $0 (name)"; exit 1; }
kill -HUP $(cat "$1".pid)
