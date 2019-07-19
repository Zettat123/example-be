USE mysql;
UPDATE user SET plugin='mysql_native_password' WHERE User='root';
FLUSH PRIVILEGES;
CREATE DATABASE `example` CHARACTER SET utf8mb4;