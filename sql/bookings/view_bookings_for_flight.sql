SELECT 
    B.Id AS BookingId,
    P.Name AS PassengerName,
    P.Nationality,
    F.Id AS FlightId,
    DA.Name AS DepartureAirport,
    AA.Name AS DestinationAirport,
    F.DepartureDateTime,
    B.Date AS BookingDate,
    B.Time AS BookingTime,
    B.SeatNumber,
    B.TravelClass
FROM Booking B
JOIN Passenger P ON B.PassengerId = P.Id
JOIN Flight F ON B.FlightId = F.Id
JOIN Airport DA ON F.DepartureAirportId = DA.Id
JOIN Airport AA ON F.DestinationAirportId = AA.Id
WHERE B.FlightId = :flight_id
ORDER BY B.SeatNumber;