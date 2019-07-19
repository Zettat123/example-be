#!/bin/bash
if [ -f "/var/run/apache2/apache2.pid" ];then
rm -f /var/run/apache2/apache2.pid
fi

find /var/lib/mysql -type f -exec touch {} \; && service mysql start

python3 initdb.py
python3 exampleserver.py
