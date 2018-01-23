#!/usr/bin/env bash
python -m SimpleHTTPServer 9090 &
PID=$!
echo $PID > web.pid
wait $PID
