-- Script: Create the table second_table and add multiple rows

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS @database_name.second_table (
  id INT,
  name VARCHAR(256),
  score INT
);

-- Insert multiple rows
INSERT INTO @database_name.second_table (id, name, score)
VALUES (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);

