SELECT
    P.Name AS PassengerName,
    P.Nationality,
    B.SeatNumber,
    B.TravelClass
FROM Passenger P
JOIN Booking B ON P.Id = B.PassengerId
WHERE B.FlightId = :flight_id;