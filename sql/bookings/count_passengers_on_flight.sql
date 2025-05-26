SELECT COUNT(DISTINCT Id) AS passenger_count
FROM Booking
WHERE FlightId = :flight_id; 