#!/bin/bash
PID=$(cat service_layer.pid)
kill -HUP $PID
