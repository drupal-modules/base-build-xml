#!/usr/bin/env bash
php -S 127.0.0.1:18888 --define auto_prepend_file=../tests/includes/runserver-prepend.php > php.log &
PID=$!
echo $PID > php_web.pid
wait $PID
