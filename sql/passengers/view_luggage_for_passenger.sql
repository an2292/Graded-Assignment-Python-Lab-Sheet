SELECT 
    P.Name AS PassengerName,
    P.Nationality,
    L.TagNumber,
    L.Weight AS WeightKg,
    F.Id AS FlightId,
    DA.Name AS DepartureAirport,
    AA.Name AS DestinationAirport,
    F.DepartureDateTime
FROM Passenger P
JOIN Luggage L ON P.Id = L.PassengerId
JOIN Flight F ON L.FlightId = F.Id
JOIN Airport DA ON F.DepartureAirportId = DA.Id
JOIN Airport AA ON F.DestinationAirportId = AA.Id
WHERE P.Id = :passenger_id
ORDER BY L.TagNumber;