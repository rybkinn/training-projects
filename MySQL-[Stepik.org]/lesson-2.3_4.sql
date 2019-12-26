SELECT g.name as good_name, c.name as category_name FROM category_has_good as chg
    LEFT OUTER JOIN category as c
        ON chg.category_id = c.id
    RIGHT OUTER JOIN good as g
        ON chg.good_id = g.id
UNION
SELECT g.name as good_name, c.name as category_name FROM category_has_good as chg
    RIGHT OUTER JOIN category as c
        ON chg.category_id = c.id
    LEFT OUTER JOIN good as g
        ON chg.good_id = g.id
    WHERE g.name is NULL;
