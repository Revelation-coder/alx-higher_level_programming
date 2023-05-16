-- Script: Display top 3 cities temperature during July and August ordered by temperature (descending)

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- Retrieve the top 3 cities with the highest temperatures during July and August
SELECT city, temperature
FROM @database_name.download
WHERE month IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;
