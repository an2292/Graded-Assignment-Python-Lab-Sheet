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
    B.SeatNumber,
    B.TravelClass
FROM Booking B
JOIN Passenger P ON B.PassengerId = P.Id
JOIN Flight F ON B.FlightId = F.Id
JOIN Airport DA ON F.DepartureAirportId = DA.Id
JOIN Airport AA ON F.DestinationAirportId = AA.Id
WHERE B.Date BETWEEN :start_date AND :end_date
ORDER BY B.Date, B.Time;