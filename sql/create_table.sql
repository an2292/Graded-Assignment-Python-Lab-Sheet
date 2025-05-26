-- Drop tables in reverse order due to foreign key constraints
-- For testing and demo purposes, dropping would be handled in the application logic for real-life
-- use cases.
DROP TABLE IF EXISTS Crew_Assignment;
DROP TABLE IF EXISTS Pilot_Assignment;
DROP TABLE IF EXISTS Luggage;
DROP TABLE IF EXISTS Booking;
DROP TABLE IF EXISTS Passenger;
DROP TABLE IF EXISTS Cabin_Crew;
DROP TABLE IF EXISTS Pilot;
DROP TABLE IF EXISTS Flight;
DROP TABLE IF EXISTS Airport;

CREATE TABLE Airport (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Country TEXT NOT NULL
);

CREATE TABLE Flight (
    Id INTEGER PRIMARY KEY,
    DepartureAirportId INTEGER NOT NULL,
    DestinationAirportId INTEGER NOT NULL,
    Duration INTEGER NOT NULL, -- in minutes
    Price REAL NOT NULL,
    FOREIGN KEY (DepartureAirportId) REFERENCES Airport(Id),
    FOREIGN KEY (DestinationAirportId) REFERENCES Airport(Id)
);

CREATE TABLE Pilot (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Role TEXT NOT NULL
);

CREATE TABLE Cabin_Crew (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Role TEXT NOT NULL
);

CREATE TABLE Passenger (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Nationality TEXT NOT NULL,
    DateOfBirth DATE NOT NULL
);

CREATE TABLE Booking (
    Id INTEGER PRIMARY KEY,
    FlightId INTEGER NOT NULL,
    PassengerId INTEGER NOT NULL,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    SeatNumber TEXT NOT NULL,
    TravelClass TEXT NOT NULL,
    FOREIGN KEY (FlightId) REFERENCES Flight(Id),
    FOREIGN KEY (PassengerId) REFERENCES Passenger(Id)
);

CREATE TABLE Luggage (
    TagNumber TEXT PRIMARY KEY,
    PassengerId INTEGER NOT NULL,
    FlightId INTEGER NOT NULL,
    Weight REAL NOT NULL,
    FOREIGN KEY (PassengerId) REFERENCES Passenger(Id),
    FOREIGN KEY (FlightId) REFERENCES Flight(Id)
);

CREATE TABLE Pilot_Assignment (
    PilotId INTEGER NOT NULL,
    FlightId INTEGER NOT NULL,
    PRIMARY KEY (PilotId, FlightId),
    FOREIGN KEY (PilotId) REFERENCES Pilot(Id),
    FOREIGN KEY (FlightId) REFERENCES Flight(Id)
);

CREATE TABLE Crew_Assignment (
    CrewId INTEGER NOT NULL,
    FlightId INTEGER NOT NULL,
    PRIMARY KEY (CrewId, FlightId),
    FOREIGN KEY (CrewId) REFERENCES Cabin_Crew(Id),
    FOREIGN KEY (FlightId) REFERENCES Flight(Id)
);

