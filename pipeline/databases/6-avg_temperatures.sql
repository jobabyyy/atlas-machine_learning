-- dump import and calc avg temp(F) in all cities
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;