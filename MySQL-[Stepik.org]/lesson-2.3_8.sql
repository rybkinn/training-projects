SELECT s.name source_name FROM source s
	WHERE NOT EXISTS (SELECT * FROM client c WHERE c.source_id = s.id)
UNION
SELECT so.name source_name FROM source so
    JOIN client cl ON cl.source_id = so.id
    JOIN sale sa ON sa.client_id = cl.id
    JOIN status st ON st.id = sa.status_id WHERE st.name = "rejected"