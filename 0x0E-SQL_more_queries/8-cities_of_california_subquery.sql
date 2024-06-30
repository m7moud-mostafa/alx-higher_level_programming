-- lists all the cities of california in th data base
SELECT c.id, c.name
FROM cities AS c
JOIN states AS s ON c.state_id = s.id
WHERE c.state_id = 1
ORDER BY c.id ASC;
