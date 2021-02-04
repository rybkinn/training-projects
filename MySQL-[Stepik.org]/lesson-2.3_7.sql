SELECT c.name, COUNT(shg.sale_id) FROM sale_has_good shg
    RIGHT JOIN category_has_good chg ON shg.good_id = chg.good_id
    RIGHT JOIN category c ON chg.category_id = c.id
    GROUP BY c.name