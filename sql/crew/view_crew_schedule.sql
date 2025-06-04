SELECT
    C.Name AS CrewName,
    C.Role AS CrewRole,
    CA.FlightId,
    DA.Name AS DepartureAirport,
    AA.Name AS DestinationAirport,
    F.DepartureDateTime,
    F.Status
FROM Cabin_Crew C
JOIN Crew_Assignment CA ON C.Id = CA.CrewId
JOIN Flight F ON CA.FlightId = F.Id
JOIN Airport DA ON F.DepartureAirportId = DA.Id
JOIN Airport AA ON F.DestinationAirportId = AA.Id
WHERE C.Id = :crew_id
ORDER BY F.DepartureDateTime; 