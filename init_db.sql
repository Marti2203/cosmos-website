CREATE DATABASE cosmos_website_test CHARACTER SET UTF8;
CREATE USER cosmos_website_tester@localhost IDENTIFIED BY '2020123';
GRANT ALL PRIVILEGES ON cosmos_website_test.* TO cosmos_website_tester@localhost;
FLUSH PRIVILEGES;
