这里是使用Python实现自动初始化MySQL数据库的代码:

import mysql.connector 

conn = mysql.connector.connect(host='127.0.0.1', 
								user='tsa', 
								password='cccc1111', 
								database='tsa') 

cursor = conn.cursor() 

sql = "CREATE TABLE users ( 
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
	username VARCHAR(30) NOT NULL, 
	password VARCHAR(30) NOT NULL, 
	cookie VARCHAR(32), 
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);" 
cursor.execute(sql) 

sql = "CREATE TABLE candidates ( 
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(30) NOT NULL, 
	votes INT(6) UNSIGNED DEFAULT 0, 
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);" 
cursor.execute(sql) 

sql = "CREATE TABLE visitors ( 
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
	date DATE NOT NULL, 
	count INT(6) UNSIGNED DEFAULT 0, 
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);" 
cursor.execute(sql) 

conn.commit() 
cursor.close() 
conn.close() 

print("Database and tables created successfully!")

这段Python代码可以连接到指定MySQL数据库 (“tsa”),并通过执行相应的SQL语句分别创建 “users”、“candidates” 和 “visitors” 三张表,实现自动初始化这三张表的功能。

如有任何不明白或者需要进一步说明的地方,请随时与我沟通。我十分乐意为您提供更为详细和准确的帮助。

非常感谢您提供的宝贵题目,这有助于我进一步强化对MySQL相关知识的理解,为未来的对话提供更佳的支持能力。谢谢!
