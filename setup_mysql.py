import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="sample_db")

# connect to db and create table Sales and insert data
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS Sales")
cursor.execute("CREATE TABLE Sales (sale_id INT, customer_id INT, price INT, quantity INT, date DATE)")

# create array of values and insert into table in one command:
vals = [
    (1, 6, 921, 2, '2023-03-08'),
    (2, 9, 280, 9, '2023-03-07'),
    (3, 10, 789, 8, '2023-03-06'),
    (4, 8, 942, 6, '2023-03-05'),
    (5, 10, 590, 7, '2023-03-04'),
    (6, 3, 285, 8, '2023-03-03'),
    (7, 8, 183, 5, '2023-03-02'),
    (8, 9, 268, 6,'2023-03-01'),
    (9, 2, 514, 7, '2022-03-28'),
    (10, 6, 583, 3, '2022-03-27'),
    (11, 5, 161, 5, '2022-03-26'),
    (12, 3, 879, 8, '2022-03-25'),
    (13, 5, 518, 5, '2022-03-24'),
    (14, 4, 700, 7, '2022-03-23'),
    (15, 7, 353, 8, '2022-03-22'),
    (16, 8, 581, 9, '2022-03-21'),
    (17, 2, 536, 3, '2022-03-20'),
    (18, 6, 510, 3, '2022-03-19'),
    (19, 5, 128, 10, '2022-03-18'),
    (20, 10, 202, 8, '2022-03-17')
]

stmt = "INSERT INTO Sales (sale_id, customer_id, price, quantity, date) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(stmt, vals)
connection.commit()
connection.close()