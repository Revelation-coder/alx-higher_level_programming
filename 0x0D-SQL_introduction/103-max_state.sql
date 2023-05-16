-- Script: Display max temperature of each state ordered by State name
SELECT state, MAX(temperature) AS max_temperature
FROM hbtn_0c_0.temperatures
GROUP BY state
ORDER BY state;
