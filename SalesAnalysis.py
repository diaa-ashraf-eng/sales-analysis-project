import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db_of_sales"
)
mycursor=mydb.cursor(buffered=True)

"""databs="CREATER DATABASE db_of_sales"
mycursor.execute(databs)"""

"""tbl="CREATE TABLE sales(id INT AUTO_INCREMENT PRIMARY KEY,product_name VARCHAR(50),category VARCHAR(50),price INT,quantity INT)"
mycursor.execute(tbl)"""

"""
data_entry="INSERT INTO sales (product_name, category, price, quantity) VALUES (%s,%s,%s,%s)"
data=[
('Laptop', 'Electronics', 10000, 5),
('Phone', 'Electronics', 5000, 10),
('Headphones', 'Electronics', 500, 15),
('Shirt', 'Clothes', 300, 20),
('Jeans', 'Clothes', 700, 10),
('Shoes', 'Clothes', 1000, 8),
('Watch', 'Accessories', 1500, 7),
('Bag', 'Accessories', 800, 12),
('Sunglasses', 'Accessories', 400, 10),
('Tablet', 'Electronics', 6000, 4)
]
mycursor.executemany(data_entry,data)
mydb.commit() 
"""

"""out="SELECT * FROM sales"
mycursor.execute(out)
rows=mycursor.fetchall()
for row in rows:
   print(row)"""


#getting number of products
n_prod="SELECT COUNT(id) FROM sales"
mycursor.execute(n_prod)
num,=mycursor.fetchone()
print(F"Number of Products is {num}\n")

#total quantity of sales
total="SELECT SUM(quantity) FROM sales"
mycursor.execute(total)
tot_quant, =mycursor.fetchone()
print(F"The total Quantity of the sales is {tot_quant}\n")

#total money
money="SELECT SUM(price * quantity) FROM sales"
mycursor.execute(money)
profit, =mycursor.fetchone()
print(f"The total profit is {profit:,} EGP\n")

#number of products in each category
num="SELECT COUNT(product_name),category FROM sales GROUP BY category"
mycursor.execute(num)
products=mycursor.fetchall()
for product in products:
    print(F"{product[1]} contain {product[0]} products")

#most selling category
sell="SELECT category, SUM(quantity) AS sum FROM sales GROUP BY category ORDER BY sum DESC"
mycursor.execute(sell)
most_cat=mycursor.fetchone()
print(F"\nThe most selling Catogery is {most_cat[0]} with {most_cat[1]} sold piece\n")

#most expensive product
expensive="SELECT product_name,price FROM sales ORDER BY price DESC LIMIT 1"
mycursor.execute(expensive)
product=mycursor.fetchone()
print(F"The most Expensive product is {product[0]} with price {product[1]:,} EGP\n")

#adding column in TABLE sales
"""add="ALTER TABLE sales ADD COLUMN customer_id INT"
mycursor.execute(add)"""

#update data in table sales

# update="""UPDATE sales SET customer_id=CASE
#    WHEN id IN (1,4) THEN 1
#    WHEN id IN (2,5) THEN 2
#    WHEN id IN (3,6) THEN 3
#    WHEN id IN (7,8) THEN 4
#    WHEN id IN (9,10) THEN 5 
# END
# WHERE id BETWEEN 1 And 10"""

# mycursor.execute(update)
# mydb.commit()

#create new table
"""table="CREATE TABLE customers (customer_id INT AUTO_INCREMENT PRIMARY KEY," \
"customer_name VARCHAR(30),city VARCHAR(30))"
mycursor.execute(table)"""

#intering data to customers table
"""customer="INSERT INTO customers (customer_name,city) VALUES(%s,%s)"
data=[
      ('Ahmed','Cairo'),
      ('Mohamed','Tanta'),
      ('Sara','Giza'),
      ('Mona','Mansoura'),
      ('Rawan','Alexandria')
      ]
mycursor.executemany(customer,data)
mydb.commit()"""

#each purchase process with the name of customer,product,number using inner join
join="SELECT customers.customer_name, sales.product_name, sales.quantity FROM sales INNER JOIN customers " \
"ON sales.customer_id = customers.customer_id"
mycursor.execute(join)
process=mycursor.fetchall()
print("##purchase processes##")
for p in process:
    print(F"{p[0]} bought {p[2]} {p[1]}")
print("\n") 

#how much each customer buy
buy="SELECT customers.customer_name, SUM(sales.quantity * sales.price) AS money FROM sales INNER JOIN customers " \
"ON sales.customer_id = customers.customer_id GROUP BY customers.customer_name ORDER BY money DESC"
mycursor.execute(buy)
tot_spent=mycursor.fetchall()
for t in tot_spent:
    print(F"{t[0]} bought with total {t[1]:,} EGP")
print("\n")

#the most customer spent money
most="""
SELECT customers.customer_name, SUM(sales.quantity * sales.price) AS money
FROM sales INNER JOIN customers
ON sales.customer_id = customers.customer_id
GROUP BY customer_name ORDER BY money DESC
"""
mycursor.execute(most)
cust=mycursor.fetchone()
print(F"The most customer spent money is {cust[0]} with {cust[1]:,} EGP")