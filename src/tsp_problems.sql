use s5094922db;
SET FOREIGN_KEY_CHECKS = 0;
Drop table IF EXISTS Nodes;
Drop table IF EXISTS Solutions;
Drop table IF EXISTS Problems;
Drop table IF EXISTS Solution_Nodes;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE Problems (
    Name VARCHAR(32),
    Dimension INTEGER(11),
    Primary Key (Name)
);

CREATE TABLE Nodes (
    Name VARCHAR(32),
    ID INTEGER,
    x float(3),
    y float(3),
    Primary Key (Name,ID)
);

CREATE TABLE Solutions (
    Problem_Name VARCHAR (32),
    TourLength float(2),
    Algorithm VARCHAR(32),
    RunningTime INTEGER(11),
    Primary Key(Problem_Name,RunningTime)
);

CREATE TABLE Solution_Nodes (
    Name VARCHAR(32),
    ID INTEGER(11),
    RunningTime INTEGER(11),
    Solve_Order_Id INTEGER(11),
    x float(3),
    y float(3),
    Primary Key (Name,ID,RunningTime)
);