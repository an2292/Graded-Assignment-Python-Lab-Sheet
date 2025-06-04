SELECT 
    C.Id AS CrewId,
    C.Name AS CrewName,
    C.Role AS CrewRole,
    COUNT(DISTINCT CA.FlightId) AS AssignedFlights
FROM Cabin_Crew C
LEFT JOIN Crew_Assignment CA ON C.Id = CA.CrewId
GROUP BY C.Id, C.Name, C.Role
ORDER BY C.Role, C.Name; 