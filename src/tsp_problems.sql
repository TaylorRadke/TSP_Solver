Drop table IF EXISTS Nodes;
Drop table IF EXISTS Solutions;
Drop table IF EXISTS Problem;

CREATE TABLE Problem (
    Name VARCHAR(32),
    Dimension INTEGER(11),
    Primary Key (Name)
);

CREATE TABLE Nodes (
    Name VARCHAR(32) ,
    ID INTEGER,
    x float(3),
    y float(3),
    Primary Key (Name,ID)
);

CREATE TABLE Solutions (
    Problem_Name VARCHAR (32),
    SolutionID INTEGER(11),
    TourLength float(2),
    Algorithms VARCHAR(32),
    RunningTime INTEGER(11),
    Primary Key(SolutionID),
    Foreign Key(Problem_Name) References Problem(Name)
);