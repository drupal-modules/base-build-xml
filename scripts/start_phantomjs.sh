#!/bin/bash
/usr/local/bin/phantomjs --webdriver='127.0.0.1:18889' &
PID=$!
echo $PID > phantomjs.pid
wait $PID
