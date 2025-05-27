SELECT 
    F.Id AS FlightId,
    DA.Name AS DepartureAirport,
    DA.Country AS DepartureCountry,
    AA.Name AS DestinationAirport,
    AA.Country AS DestinationCountry,
    F.Duration AS DurationMinutes,
    F.Price,
    F.Status,
    F.DepartureDateTime
FROM Flight F
JOIN Airport DA ON F.DepartureAirportId = DA.Id
JOIN Airport AA ON F.DestinationAirportId = AA.Id
WHERE F.DepartureAirportId = :departure_id
ORDER BY F.DepartureDateTime;