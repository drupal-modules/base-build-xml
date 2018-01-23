#!/bin/bash
PID=$(cat phantomjs.pid)
kill -HUP $PID
