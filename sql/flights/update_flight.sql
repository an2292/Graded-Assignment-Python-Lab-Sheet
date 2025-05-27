UPDATE Flight 
SET 
    DepartureAirportId = :departure_airport_id,
    DestinationAirportId = :destination_airport_id,
    Duration = :duration,
    Price = :price
WHERE Id = :flight_id;
