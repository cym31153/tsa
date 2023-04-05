import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="tsa",
  password="cccc1111"
)

# Create a new database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE tsa")
mycursor.execute("USE tsa")

# Create a new table for users
mycursor.execute("CREATE TABLE users (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, username VARCHAR(30) NOT NULL, password VARCHAR(30) NOT NULL, cookie VARCHAR(32), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# Create a new table for candidates
mycursor.execute("CREATE TABLE candidates (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL, votes INT(6) UNSIGNED DEFAULT 0, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# Create a new table for visitors
mycursor.execute("CREATE TABLE visitors (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, date DATE NOT NULL, count INT(6) UNSIGNED DEFAULT 0, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# Commit changes and close connection
mydb.commit()
mycursor.close()
mydb.close()
