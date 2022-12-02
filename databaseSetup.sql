--SQL DATABASE SETUP--
CREATE DATABASE IF NOT EXISTS RossPaintingsData

--CREATE tables that hold data--
CREATE TABLE Paintings (
        id INT NOT NULL PRIMARY KEY,
        name VARCHAR(300),
        date VARCHAR(100),
        month INT,
        image VARCHAR(300),
        video VARCHAR(300)
);
CREATE TABLE Colors (
        name VARCHAR(300) NOT NULL PRIMARY KEY,
        hexcode VARCHAR(300),
);
CREATE TABLE Objects (
        name VARCHAR(300) NOT NULL PRIMARY KEY,
;)

-- CREATE join tables for colors and objects -- 
CREATE TABLE paintingColors (
        paintingId INT NOT NULL,
        colorName VARCHAR(300) NOT NULL,
        FOREIGN KEY(paintingId)
            REFERENCES Paintings(id)
            ON DELETE CASCADE
        FOREIGN KEY(colorName)
            REFERENCES Colors(name)
            ON DELETE CASCADE
);

CREATE TABLE paintingObjects (
        paintingId INT NOT NULL,
        objectName VARCHAR(300) NOT NULL,
        FOREIGN KEY(paintingId)
            REFERENCES Paintings(id)
            ON DELETE CASCADE
        FOREIGN KEY(objectName)
            REFERENCES Objects(name)
            ON DELETE CASCADE
);
