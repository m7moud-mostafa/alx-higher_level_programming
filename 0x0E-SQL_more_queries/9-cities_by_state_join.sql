-- lists cities contained in the database
SELECT c.id, c.name, s.name
FROM cities AS c
LEFT JOIN states AS s
ON s.id = c.state_id
ORDER BY c.id ASC;
