SELECT 
    P.Id AS PilotId,
    P.Name AS PilotName,
    P.Role AS PilotRole,
    COUNT(DISTINCT PA.FlightId) AS AssignedFlights
FROM Pilot P
LEFT JOIN Pilot_Assignment PA ON P.Id = PA.PilotId
GROUP BY P.Id, P.Name, P.Role
ORDER BY P.Role, P.Name; 