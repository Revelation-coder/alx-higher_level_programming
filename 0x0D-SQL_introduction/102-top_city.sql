-- Script: Display top 3 cities temperature during July and August ordered by temperature
SELECT city, temperature
FROM hbtn_0c_0.temperatures
WHERE month IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;
