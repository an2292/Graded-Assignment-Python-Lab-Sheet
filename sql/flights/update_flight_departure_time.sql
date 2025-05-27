UPDATE Flight
SET DepartureDateTime = :new_departure_datetime
WHERE Id = :flight_id;