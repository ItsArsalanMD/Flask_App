# while installing mysql

set default password to 123

by using 

login to mysql

$ sudo mysql -u root -p
$ USE mysql;
$ ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123';
# FLUSH PRIVILEGES;
$ EXIT;

