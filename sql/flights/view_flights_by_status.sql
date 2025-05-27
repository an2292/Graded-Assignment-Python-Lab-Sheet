SELECT
    F.Id AS FlightId,
    DA.Name AS DepartureAirport,
    AA.Name AS DestinationAirport,
    F.Duration,
    F.Price,
    F.Status,
    F.DepartureDateTime
FROM Flight F
JOIN Airport DA ON F.DepartureAirportId = DA.Id
JOIN Airport AA ON F.DestinationAirportId = AA.Id
WHERE F.Status = :status;