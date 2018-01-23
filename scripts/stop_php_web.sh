#!/bin/bash
PID=$(cat php_web.pid)
kill -HUP $PID
