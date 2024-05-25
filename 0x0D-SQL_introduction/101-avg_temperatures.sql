-- Imports tabledump file into database.
USE hbtn_0c_0;

source ./temperatures.sql;

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
