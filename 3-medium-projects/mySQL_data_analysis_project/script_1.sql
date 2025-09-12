tee output_1.txt

show databases;

use restaurant_db;

show tables;

select * from order_details limit 30;

select min(order_date), max(order_date) from order_details;

select count(distinct order_id) from order_details;

select count(*) as num_items from order_details;

select order_id, count(*) as num_orders from order_details group by order_id order by num_orders desc limit 30;

select order_id, count(*) as num_orders from order_details group by order_id having num_orders > 12;

notee