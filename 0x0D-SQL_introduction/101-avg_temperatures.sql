-- Script: Display average temperature (Fahrenheit) by city ordered by temperature (descending order)
SELECT city, AVG(temperature) AS avg_temperature
FROM hbtn_0c_0.temperatures
GROUP BY city
ORDER BY avg_temperature DESC;
