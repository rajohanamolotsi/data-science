# Data Analyst Portfolio Project: Restaurant Order Analysis in SQL
# Objective 1
## EXPLORE THE ITEMS TABLE

### 1. View the menu_items table and write a query to find the number of items on the menu.

`select count(*) from menu_items`

ANS: There are `32 items` on the menu

---

- <span style="color: red;"> `Correct!` </span>

---

### 2.  View the menu_items table and write a query to find the number of items on the menu.

`select * from menu_items order by price;`

`avg_price = 13.285938`

ANS: I would say the meals costing `17.95` and `19.95` are the most expensive, namely

- Edamane
- Mac & Cheese
- French Fries
- Chips & Salsa
- Hot Dog
- Potstickers
- Chips & Guacamole

AND

- Korean Beef Bowl
- Pork Ramen
- Spaghetti & Meatballs
- Meat Lasagna
- Chicken Parmesan
- Shrimp Scampi,

respectfully.

---

- <span style="color: red;"> Partially correct because I listed items on the menu `3 units` away from the mean, which is not bad in my own opinion. </span>
- <span style="color: red;"> I also made a mistake by repeating the question above and the answers do not even belong here. </span>

---

### 3. How many Italian dishes are on the menu? What are the least and most expensive Italian dishes on the menu?

`select count(*) from menu_items where category = 'Italian';`

`select item_name, price from menu_items where category = 'Italian' order by price;`

ANS: There are `9 Italian dishes` on the menu. The least and most expensive Italian dishes are `Spaghetti`, `Fettuccine Alfredo` and `Shrimp Scampi` respectfully.

---
- <span style="color: red;"> `Correct!` </span>
- <span style="color: red;"> The instructor also made a mistake by only looking at `Spaghetti`, thus overlooking `Fettuccine Alfredo`. </span>
---


### How many dishes are in each category? What is the average dish price within each category?

To find the number of dishes in each category:

`select count(*) from menu_items where category = '[category name]'`

To find the average dish price within each category:

`select avg(price) as avg_price from menu_items where category = '[category name]'`

ANS:

- American: `6 dishes, 10.07 average price`
- Asian: `8 dishes, average price: 13.48`
- Mexican: `9 dishes, average price 11.8`
- Italian: `9 dishes, average price 16.75`

---
- <span style="color: red;"> `Correct!` </span>
- <span style="color: red;"> Here I got all the numbers correct but I took the long route, I need to learn the most efficient of doing this! </span>

---

