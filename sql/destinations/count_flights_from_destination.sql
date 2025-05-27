SELECT 
    A.Id AS AirportId,
    A.Name AS AirportName,
    A.Country,
    COUNT(F.Id) AS FlightsFromDestination
FROM Airport A
LEFT JOIN Flight F ON A.Id = F.DepartureAirportId
WHERE A.Id = :departure_id
GROUP BY A.Id, A.Name, A.Country;