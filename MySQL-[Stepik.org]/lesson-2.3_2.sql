SELECT first_name, last_name, COUNT(status.id) as new_sale_name FROM sale
    INNER JOIN status
        ON sale.status_id = status.id
    INNER JOIN client
        ON sale.client_id = client.id
        WHERE status.name = 'new'
     GROUP BY sale.client_id;
