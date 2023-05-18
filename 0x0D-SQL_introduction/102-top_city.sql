-- Script: Display top 3 cities temperature during July and August ordered by temperature
SELECT city, AVG(value) AS avg_temp
FROM hbtn_0c_0.temperatures
WHERE month IN (7, 8)
ORDER BY value  DESC
LIMIT 3;
