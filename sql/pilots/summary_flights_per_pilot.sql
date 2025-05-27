SELECT
    P.Name AS PilotName,
    P.Role AS PilotRole,
    COUNT(PA.FlightId) AS NumberOfFlightsAssigned
FROM Pilot P
JOIN Pilot_Assignment PA ON P.Id = PA.PilotId
GROUP BY P.Name, P.Role
ORDER BY NumberOfFlightsAssigned DESC;