#!/bin/bash
PID=$(cat web.pid)
kill -HUP $PID
