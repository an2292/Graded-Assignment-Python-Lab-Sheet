SELECT 
    A.Id AS AirportId,
    A.Name AS AirportName,
    A.Country,
    COUNT(DISTINCT DF.Id) AS DepartingFlights,
    COUNT(DISTINCT AF.Id) AS ArrivingFlights,
    (COUNT(DISTINCT DF.Id) + COUNT(DISTINCT AF.Id)) AS TotalFlights
FROM Airport A
LEFT JOIN Flight DF ON A.Id = DF.DepartureAirportId
LEFT JOIN Flight AF ON A.Id = AF.DestinationAirportId
GROUP BY A.Id, A.Name, A.Country
ORDER BY A.Country, A.Name;