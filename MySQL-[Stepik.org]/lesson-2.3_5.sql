SELECT sr.name as source_name, SUM(sl.sale_sum) as sale_sum FROM client as c
    RIGHT OUTER JOIN sale as sl
        ON c.id = sl.client_id
    RIGHT OUTER JOIN source as sr
        ON c.source_id = sr.id
    GROUP BY sr.name;
