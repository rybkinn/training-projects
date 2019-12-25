SELECT good.name, category.name FROM category_has_good
    INNER JOIN category
    ON category_has_good.category_id = category.id
    INNER JOIN good
    ON category_has_good.good_id = good.id
    ORDER BY good.name, category.name;
