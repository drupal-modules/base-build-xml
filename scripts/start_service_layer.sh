#!/bin/bash
php -S 127.0.0.1:9090 ../includes/service_layer_route.php &
PID=$!
echo $PID > service_layer.pid
wait $PID
