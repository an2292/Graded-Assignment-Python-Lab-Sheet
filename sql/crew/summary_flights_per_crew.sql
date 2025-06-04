SELECT
    C.Name AS CrewName,
    C.Role AS CrewRole,
    COUNT(CA.FlightId) AS NumberOfFlightsAssigned
FROM Cabin_Crew C
JOIN Crew_Assignment CA ON C.Id = CA.CrewId
GROUP BY C.Name, C.Role
ORDER BY NumberOfFlightsAssigned DESC; 