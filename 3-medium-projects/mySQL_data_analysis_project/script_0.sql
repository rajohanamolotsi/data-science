use restaurant_db;

show tables;

select * from menu_items;

select * from menu_items order by price;

select * from menu_items order by price desc;

select count(menu_item_id) from menu_items;

select * from menu_items where category = 'Italian' order by price;

select * from menu_items where category = 'Italian' order by price desc;

select count(category) as Italian_dishes_count from menu_items where category = 'Italian';

select category, count(*) from menu_items group by category;

select category, avg(price) as avg_price from menu_items group by category order by avg_price desc;

