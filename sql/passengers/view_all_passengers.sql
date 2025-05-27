SELECT 
    P.Id AS PassengerId,
    P.Name AS PassengerName,
    P.Nationality,
    P.DateOfBirth,
    COUNT(B.Id) AS TotalBookings,
    COUNT(DISTINCT B.FlightId) AS UniqueFlights
FROM Passenger P
LEFT JOIN Booking B ON P.Id = B.PassengerId
GROUP BY P.Id, P.Name, P.Nationality, P.DateOfBirth
ORDER BY P.Name; 