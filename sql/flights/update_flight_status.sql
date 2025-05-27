UPDATE Flight
SET Status = :new_status
WHERE Id = :flight_id;