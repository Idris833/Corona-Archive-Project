/*SQL Statements*/
CREATE DATABASE
IF NOT EXISTS seteam32;

USE `seteam32`;

DROP TABLE IF EXISTS `Visitor`;

CREATE TABLE Visitor (
  citizen_id INTEGER NOT NULL AUTO_INCREMENT,
  visitor_name VARCHAR(45) NOT NULL,
  visitor_address VARCHAR(45) NOT NULL,
  phone_number VARCHAR(45),
  email VARCHAR(45),
  device_id VARCHAR(45) NOT NULL UNIQUE,
  infected BOOLEAN NOT NULL,
  PRIMARY KEY (citizen_id)
);

DROP TABLE IF EXISTS `Hospital`;

CREATE TABLE Hospital (
  hostipal_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(45) NOT NULL UNIQUE,
  password VARCHAR(45) NOT NULL,
  PRIMARY KEY (hostipal_id)
);

DROP TABLE IF EXISTS `Places`;

CREATE TABLE Places (
  place_id INT NOT NULL AUTO_INCREMENT,
  place_name VARCHAR(45) NOT NULL,
  place_address VARCHAR(45) NOT NULL,
  QRcode VARCHAR(100) UNIQUE,
  PRIMARY KEY (place_id)
);

DROP TABLE IF EXISTS `Agent`;

CREATE TABLE Agent (
  agent_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(45) NOT NULL UNIQUE,
  password VARCHAR(45) NOT NULL,
  PRIMARY KEY (agent_id)
);

DROP TABLE IF EXISTS `VisitorToPlaces`;

CREATE TABLE VisitorToPlaces (
  QRcode VARCHAR(45) NOT NULL,
  device_id VARCHAR(45) NOT NULL,
  entry_date DATE NOT NULL,
  entry_time VARCHAR(45) NOT NULL,
  exit_date DATE NOT NULL,
  exit_time VARCHAR(45) NOT NULL,
  PRIMARY KEY (QRcode,device_id,entry_date,entry_time)
);

INSERT INTO Agent(username, password) VALUES("John", "asdas1221");
INSERT INTO Agent(username, password) VALUES("Idris", "12345678");
INSERT INTO Hospital(username, password) VALUES("Melina", "12345asd");
