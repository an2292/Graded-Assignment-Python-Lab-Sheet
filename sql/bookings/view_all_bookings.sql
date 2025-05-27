SELECT 
    B.Id AS BookingId,
    B.Date AS BookingDate,
    B.Time AS BookingTime,
    P.Name AS PassengerName,
    P.Nationality,
    F.Id AS FlightId,
    DA.Name AS DepartureAirport,
    AA.Name AS DestinationAirport,
    F.DepartureDateTime,
    F.Status AS FlightStatus,
    B.SeatNumber,
    B.TravelClass
FROM Booking B
JOIN Passenger P ON B.PassengerId = P.Id
JOIN Flight F ON B.FlightId = F.Id
JOIN Airport DA ON F.DepartureAirportId = DA.Id
JOIN Airport AA ON F.DestinationAirportId = AA.Id
ORDER BY B.Date DESC, B.Time DESC; 