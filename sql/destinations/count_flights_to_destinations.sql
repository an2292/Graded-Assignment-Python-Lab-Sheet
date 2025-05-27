SELECT 
    A.Id AS AirportId,
    A.Name AS AirportName,
    A.Country,
    COUNT(F.Id) AS FlightsToDestination
FROM Airport A
LEFT JOIN Flight F ON A.Id = F.DestinationAirportId
WHERE A.Id = :destination_id
GROUP BY A.Id, A.Name, A.Country;