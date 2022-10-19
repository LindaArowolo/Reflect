CREATE DATABASE reflect;
USE reflect;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  region VARCHAR(255),
  hashed_password BLOB
);


CREATE TABLE tracker (
    tracker_id	INT	PRIMARY KEY AUTO_INCREMENT,
    id		INT,
    date		DATE,
    mood		INT,
    sleep		INT,
    motivation	INT,
    journal		TEXT,

    CHECK (mood BETWEEN 1 AND 5),
    CHECK (sleep BETWEEN 1 AND 5),
    CHECK (motivation BETWEEN 1 AND 5),
    FOREIGN KEY (id) REFERENCES users (id)
);

CREATE TABLE activity (
    id	int	PRIMARY KEY AUTO_INCREMENT,
    fitness INT,
    relaxation varchar(255)
);


CREATE TABLE scrapbook(
    id INT PRIMARY KEY AUTO_INCREMENT,
    image_url VARCHAR(255),
    videos	VARCHAR(255),
    voicenotes VARCHAR(255),
    doodles VARCHAR(255),
    text	text
);
