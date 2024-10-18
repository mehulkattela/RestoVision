few_shots = [ {

        'Question' : "Howmany employees in the restaurant have worked for more than 150 hours?",
        'SQLQuery' : "SELECT count(*) FROM restaurant_db.employees where hours_worked > 150",
        'SQLResult': "Result of the SQL query",
        'Answer' : "2"
},
{
        'Question' : "Find the top 5 best-selling menu items based on total sales over the past month.",
        'SQLQuery' : "SELECT mi.name AS menu_item, SUM(s.quantity) AS total_quantity_sold, SUM(s.total) AS total_revenue FROM sales s JOIN menu_items mi ON s.menu_item_id = mi.menu_item_id WHERE s.sale_date BETWEEN CURDATE() - INTERVAL 1 MONTH AND CURDATE() GROUP BY s.menu_item_id ORDER BY total_quantity_sold DESC LIMIT 5;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Medu Vada and Idli Sambar"
},
{
        'Question' : "Find the inventory items that need to be reordered soon (stock below reorder level).",
        'SQLQuery' : "SELECT item_name, stock_quantity, reorder_level, next_reorder_date FROM inventory WHERE stock_quantity < reorder_level ORDER BY next_reorder_date ASC;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "No items found. All the inventory items are in stock at the moment."
},
{
        'Question' : "Find the menu items that received an average rating of less than 4 in the last month and count the number of low ratings.",
        'SQLQuery' : "SELECT mi.name AS menu_item, AVG(cf.rating) AS avg_rating, COUNT(cf.feedback_id) AS low_rating_count FROM customer_feedback cf JOIN menu_items mi ON cf.menu_item_id = mi.menu_item_id WHERE cf.feedback_date BETWEEN CURDATE() - INTERVAL 1 MONTH AND CURDATE() GROUP BY cf.menu_item_id HAVING avg_rating < 4 ORDER BY avg_rating ASC;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Filter Coffee with avg rating of 3.0 and low rating_count is 1."
},

]