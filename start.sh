#!/bin/bash
rm -f /var/run/apache2/apache2.pid
find /var/lib/mysql -type f -exec touch {} \; && service mysql start

python initdb.py
python exampleserver.py
