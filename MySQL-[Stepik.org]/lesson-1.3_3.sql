SELECT category,SUM(price*sold_num) as revenue FROM store GROUP BY category ORDER BY revenue DESC LIMIT 5;
