import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="   ",
	database="mydb"
	)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE CUSTOMERS (name varchar(255),addess varchar(255))")

#mycursor.execute("ALTER TABLE CUSTOMERS ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#mycursor.execute("show tables")
#for i in mycursor:
#	print(i)



'''
sql="INSERT INTO CUSTOMERS (name,address) VALUES(%s,%s)"
val=[

  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633'),


]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted. ")
print("last row id is ",mycursor.lastrowid)'''

#to remove duplicates from table

'''mycursor.execute("DELETE e1 FROM CUSTOMERS e1,CUSTOMERS e2 WHERE e1.id>e2.id AND e1.name=e2.name")
mycursor.execute("SELECT * FROM CUSTOMERS")

myresult=mycursor.fetchall()
for x in myresult:
	print(x)'''


## to extract from wild card characters

'''sql="SELECT * FROM CUSTOMERS WHERE address LIKE %s"
val=("%way%",)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
for x in myresult:
	print(x)'''


## order by - sorting

'''mycursor.execute("DELETE e1 from CUSTOMERS e1,CUSTOMERS e2 WHERE e1.id>e2.id AND e1.name=e2.name")

sql="SELECT * FROM CUSTOMERS ORDER BY name "
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
	print (x)

# sort reverse order

sql="SELECT * FROM CUSTOMERS ORDER BY name desc "
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
	print (x)'''


## Drop table it will delete the table
'''
sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)'''


## Update Table ##


'''sql = "UPDATE CUSTOMERS SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount)

mycursor.execute("select * from CUSTOMERS")
myresult=mycursor.fetchall()
for i in myresult:
	print(i)'''

##  LIMIT THE RECORDS FROM QUIRY

'''mycursor.execute("SELECT * FROM CUSTOMERS LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x) '''
  