SELECT * FROM Flight
WHERE Price BETWEEN :min_price AND :max_price;