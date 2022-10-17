CREATE DATABASE Reflect;
USE Reflect;

CREATE TABLE Users (
user_id		INT PRIMARY KEY AUTO_INCREMENT,
email		VARCHAR(255) UNIQUE,
name		VARCHAR(255),
region		VARCHAR(255),
password	VARCHAR(255)
);

CREATE TABLE Tracker (
tracker_id	INT	PRIMARY KEY AUTO_INCREMENT,
user_id		INT,
date		DATE,
mood		INT,
sleep		INT,
motivation	INT,
journal		TEXT,

CHECK (mood BETWEEN 1 AND 5),
CHECK (sleep BETWEEN 1 AND 5),
CHECK (motivation BETWEEN 1 AND 5),
FOREIGN KEY (user_id) REFERENCES Users (user_id)
);

