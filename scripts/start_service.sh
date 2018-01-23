#!/usr/bin/env bash
[ $# -eq 0 ] && { echo "Usage: $0 (name) (router_script)"; exit 1; }
php -S 127.0.0.1:9090 $2 &
PID=$!
echo $PID > "$1".pid
wait $PID
