-- creates database and tables
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, CONSTRAINT states_pk PRIMARY KEY (id));
