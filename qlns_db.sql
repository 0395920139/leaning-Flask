create database qlns;
use qlns;
CREATE TABLE employee(
	id INT(36) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(50) NOT NULL ,
    phone varchar(50) NOT NULL,
    address varchar(255) NOT NULL
)