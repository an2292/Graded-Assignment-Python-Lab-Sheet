SELECT
    P.Name AS PilotName,
    P.Role AS PilotRole,
    PA.FlightId,
    DA.Name AS DepartureAirport,
    AA.Name AS DestinationAirport,
    F.DepartureDateTime,
    F.Status
FROM Pilot P
JOIN Pilot_Assignment PA ON P.Id = PA.PilotId
JOIN Flight F ON PA.FlightId = F.Id
JOIN Airport DA ON F.DepartureAirportId = DA.Id
JOIN Airport AA ON F.DestinationAirportId = AA.Id
WHERE P.Id = :pilot_id
ORDER BY F.DepartureDateTime;