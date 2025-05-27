UPDATE Airport 
SET 
    Name = :name,
    Country = :country
WHERE Id = :destination_id;
