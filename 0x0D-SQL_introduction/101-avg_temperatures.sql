-- Script to  Display average temperature (Fahrenheit) by city ordered by temperature (descending order)

SELECT city, AVG(value) AS avg_temp
FROM hbtn_0c_0.temperatures
GROUP BY city
ORDER BY value DESC;
