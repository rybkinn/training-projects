SELECT g.name as good_name FROM category_has_good as chg
	JOIN good as g
		ON chg.good_id = g.id
	JOIN category as c
		ON chg.category_id = c.id
			WHERE c.name = 'Cakes'
UNION
SELECT g.name as good_name FROM sale
	JOIN sale_has_good as shg
		ON shg.sale_id = sale.id
	JOIN good as g
		ON g.id = shg.good_id
	JOIN status
		ON status.id = sale.status_id
			WHERE status.name = 'delivering'
				ORDER BY good_name