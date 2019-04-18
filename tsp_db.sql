use s5094922db;
Drop TABLE Problem;
Drop TABLE Cities;
Drop TABLE Solution;
-- Table structure for table 'Problem'
--
CREATE TABLE Problem (
  Name varchar(32) NOT NULL,
  Size int(11) NOT NULL,
  Comment varchar(255) DEFAULT NULL,
  CONSTRAINT PPK PRIMARY KEY (Name)
);

--
-- Table structure for table 'Cities'
--
CREATE TABLE Cities (
  Name varchar(32) NOT NULL,
  ID int(11) NOT NULL,
  x double NOT NULL,
  y double NOT NULL,
  CONSTRAINT CPK PRIMARY KEY (Name, ID),
  CONSTRAINT PName FOREIGN KEY (Name) REFERENCES Problem (Name) ON DELETE CASCADE
); 

--
-- Table structure for table 'Solution'
--
CREATE TABLE  Solution (
  SolutionID int(11) NOT NULL AUTO_INCREMENT,
  ProblemName varchar(32) NOT NULL,
  TourLength double NOT NULL,
  Date date DEFAULT NULL,
  Author varchar(32) DEFAULT NULL,
  Algorithm varchar(32) DEFAULT NULL,
  RunningTime int(11) DEFAULT NULL,
  Tour mediumtext NOT NULL,
  CONSTRAINT SPK PRIMARY KEY (SolutionID),
  CONSTRAINT SolPName FOREIGN KEY (ProblemName) REFERENCES Problem (Name) ON DELETE CASCADE
);