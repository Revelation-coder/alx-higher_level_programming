-- Script: Convert hbtn_0c_0 database, first_table table, and name field to UTF8

-- Set the database and table names
SET @database_name = 'hbtn_0c_0';
SET @table_name = 'first_table';

-- Alter the database character set and collation
ALTER DATABASE @database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter the table character set and collation
ALTER TABLE @database_name.@table_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter the field character set and collation
ALTER TABLE @database_name.@table_name MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

