SELECT 
    F.Id AS FlightId,
    DA.Name AS DepartureAirport,
    AA.Name AS DestinationAirport,
    F.DepartureDateTime,
    COUNT(PA.PilotId) AS PilotsAssigned
FROM Flight F
LEFT JOIN Pilot_Assignment PA ON F.Id = PA.FlightId
JOIN Airport DA ON F.DepartureAirportId = DA.Id
JOIN Airport AA ON F.DestinationAirportId = AA.Id
WHERE F.Id = :flight_id
GROUP BY F.Id, DA.Name, AA.Name, F.DepartureDateTime;