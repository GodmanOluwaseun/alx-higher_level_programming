-- Displays top 3 cities temperature in July and August.
SELECT `city`, AVG(`value`) AS avg_temp
FROM temperatures
WHERE `month` IN ('July', 'August')
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
