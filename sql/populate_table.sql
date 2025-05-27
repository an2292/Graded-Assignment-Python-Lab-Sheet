-- Airport 
INSERT INTO Airport (Id, Name, Country) VALUES 
  (1, 'Heathrow', 'UK'),
  (2, 'Gatwick', 'UK'),
  (3, 'Cardiff', 'UK'),
  (4, 'Paris', 'France'),
  (5, 'Amsterdam', 'Netherlands'),
  (6, 'Madrid', 'Spain'),
  (7, 'Rome', 'Italy'),
  (8, 'Athens', 'Greece'),
  (9, 'Dublin', 'Ireland'),
  (10, 'Copenhagen', 'Denmark');

-- Flight
INSERT INTO Flight (Id, DepartureAirportId, DestinationAirportId, 
  Duration, Price, Status, DepartureDateTime) VALUES 
  (1, 5, 6, 321, 55.53, 'Scheduled', '2025-06-01 10:30:00'),
  (2, 9, 10, 103, 75.13, 'Scheduled', '2025-06-01 23:15:00'),
  (3, 8, 1, 284, 128.59, 'Delayed', '2025-06-05 06:00:00'),
  (4, 10, 4, 232, 345.13, 'Cancelled', '2025-06-05 07:50:00'),
  (5, 6, 8, 75, 243.09, 'Scheduled', '2025-06-06 13:15:00'),
  (6, 1, 6, 417, 467.58, 'Scheduled', '2025-06-07 18:30:00'),
  (7, 9, 8, 473, 323.17, 'Delayed', '2025-06-08 11:45:00'),
  (8, 5, 10, 262, 373.91, 'Delayed', '2025-06-09 09:20:00'),
  (9, 10, 2, 395, 234.02, 'Scheduled', '2025-06-10 14:45:00'),
  (10, 4, 2, 225, 150.13, 'Cancelled', '2025-06-10 18:00:00');

-- Pilot
INSERT INTO Pilot (Id, Name, Role) VALUES 
  (1, 'Elizabeth Jackson', 'Captain'),
  (2, 'Mary Thomas', 'Captain'),
  (3, 'William Brown', 'First Officer'),
  (4, 'Elizabeth Smith', 'Captain'),
  (5, 'Robert Johnson', 'First Officer'),
  (6, 'Patricia Brown', 'Captain'),
  (7, 'James Taylor', 'First Officer'),
  (8, 'Elizabeth Harris', 'First Officer'),
  (9, 'Mary Harris', 'Captain'),
  (10, 'Patricia Smith', 'Captain');

-- Cabin Crew
INSERT INTO Cabin_Crew (Id, Name, Role) VALUES 
  (1, 'James Johnson', 'Flight Attendant'),
  (2, 'Mary Anderson', 'Purser'),
  (3, 'Jennifer Harris', 'Purser'),
  (4, 'James Brown', 'Purser'),
  (5, 'Elizabeth White', 'Purser'),
  (6, 'Linda Thomas', 'Purser'),
  (7, 'Jennifer Johnson', 'Flight Attendant'),
  (8, 'Mary White', 'Flight Attendant'),
  (9, 'Patricia Brown', 'Flight Attendant'),
  (10, 'James Brown', 'Flight Attendant');

-- Passenger
INSERT INTO Passenger (Id, Name, Nationality, DateOfBirth) VALUES 
  (1, 'John Thomas', 'UK', '1968-07-23'),
  (2, 'James Harris', 'UK', '1996-11-28'),
  (3, 'James Johnson', 'UK', '1970-12-09'),
  (4, 'William White', 'UK', '1977-12-02'),
  (5, 'Jennifer Anderson', 'UK', '2007-01-12'),
  (6, 'James Thomas', 'UK', '1993-09-28'),
  (7, 'Elizabeth Thomas', 'UK', '1971-03-06'),
  (8, 'James Anderson', 'UK', '2006-12-07'),
  (9, 'Michael Anderson', 'UK', '1980-04-29'),
  (10, 'William White', 'UK', '1981-01-22');

-- Booking
INSERT INTO Booking (Id, FlightId, PassengerId, Date, Time, SeatNumber, TravelClass) VALUES 
  (1, 9, 4, '2023-08-03', '20:43', '30C', 'Business'),
  (2, 10, 9, '2024-11-08', '09:41', '21A', 'Economy'),
  (3, 7, 8, '2024-05-21', '18:54', '28C', 'First'),
  (4, 2, 6, '2025-03-04', '21:28', '24C', 'First'),
  (5, 10, 3, '2024-05-26', '11:59', '16A', 'Economy'),
  (6, 7, 8, '2023-07-24', '16:54', '23B', 'Business'),
  (7, 7, 10, '2025-10-05', '11:04', '29B', 'First'),
  (8, 8, 2, '2024-12-11', '03:08', '4B', 'First'),
  (9, 10, 3, '2023-02-12', '12:46', '2B', 'Business'),
  (10, 8, 5, '2024-03-16', '00:23', '13A', 'First');

-- Luggage
INSERT INTO Luggage (TagNumber, PassengerId, FlightId, Weight) VALUES 
  ('3bfdae9f', 6, 8, 24.4),
  ('a4618c60', 6, 5, 17.0),
  ('9e0ddf9b', 6, 6, 13.0),
  ('46b779f4', 5, 6, 28.7),
  ('fb27b0eb', 8, 7, 15.9),
  ('a2997e75', 2, 7, 9.3),
  ('9ef2c67b', 7, 8, 9.8),
  ('3afd8aa6', 3, 9, 18.4),
  ('06db9c4b', 6, 3, 10.7),
  ('aa27038d', 5, 4, 27.6);

-- Pilot Assignment
INSERT INTO Pilot_Assignment (PilotId, FlightId) VALUES 
  (2, 4),
  (3, 8),
  (8, 7),
  (10, 1),
  (4, 2),
  (1, 4),
  (1, 7),
  (6, 10),
  (8, 6),
  (1, 9);

-- Crew Assignment
INSERT INTO Crew_Assignment (CrewId, FlightId) VALUES 
  (4, 4),
  (2, 4),
  (6, 2),
  (4, 1),
  (10, 4),
  (4, 7),
  (6, 7),
  (6, 9),
  (1, 9);
