-- Script: Display average temperature (Fahrenheit) by city ordered by temperature (descending)

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- Calculate average temperature by city
SELECT city, AVG(temperature) AS avg_temperature
FROM @database_name.temperatures
GROUP BY city
ORDER BY avg_temperature DESC;

