import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1', user='tsa', password='cccc1111', database='tsa')

cursor = conn.cursor()

sql = "CREATE TABLE users ( id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, username VARCHAR(30) NOT NULL, password VARCHAR(30) NOT NULL, cookie VARCHAR(32), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );" cursor.execute(sql)

sql = "CREATE TABLE candidates ( id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL, votes INT(6) UNSIGNED DEFAULT 0, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );" cursor.execute(sql)

sql = "CREATE TABLE visitors ( id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, date DATE NOT NULL, count INT(6) UNSIGNED DEFAULT 0, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );" cursor.execute(sql)

conn.commit() cursor.close() conn.close()

print("Database and tables created successfully!")
