-- dump import and calc avg temp(F) in all cities
SELECT city, AVG(value) AS average_temperature FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;