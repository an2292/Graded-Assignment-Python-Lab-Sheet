SELECT
    A.Name AS DestinationAirport,
    A.Country,
    COUNT(F.Id) AS NumberOfFlights
FROM Airport A
JOIN Flight F ON A.Id = F.DestinationAirportId
GROUP BY A.Name, A.Country
ORDER BY NumberOfFlights DESC;