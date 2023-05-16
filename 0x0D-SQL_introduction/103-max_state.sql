-- Script: Display max temperature of each state ordered by State name

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- Retrieve the maximum temperature of each state
SELECT state, MAX(temperature) AS max_temperature
FROM @database_name.download
GROUP BY state
ORDER BY state;
