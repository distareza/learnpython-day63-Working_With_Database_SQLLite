# Working With Database SQLLite

SQLite Databases is default python database  
to create sqllite db with python simply add following code
>import sqllite3

to create a connection to db :
> db = sqllite3.connect("books-collection.db")

When running a python app, this database name will create automatically

![alt text](https://github.com/distareza/learnpython-day63-Working_With_Database_SQLLite/blob/master/resources/file_structure_db_created.png?raw=true)

Next we need to create a cursor which will control our database.
> cursor = db.cursor()

So a cursor is also known as the mouse or pointer. If we were working in Excel or Google Sheet, we would be using the cursor to add rows of data or edit/delete data, we also need a cursor to modify our SQLite database.

To create a table
> cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

To Insert a data
> cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")  
> db.commit()

Please refer to this documentation for sql commands
https://www.codecademy.com/article/sql-commands   
  
To browse db use following app : https://sqlitebrowser.org/dl/  


# SQLAlchemy
SQLAlchemy is defined as an ORM Object Relational Mapping library. 
This means that it's able to map the relationships in the database into Objects. 
Fields become Object properties. 
Tables can be defined as separate Classes and each row of data is a new Object. 
This will make more sense after we write some code and see how we can create a Database/Table/Row of data using SQLAlchemy.

In order to run sqlalchemy it required following packages
This code works with Flask, Flask-SQLAlchemyand SQLAlchemy
![alt text](https://github.com/distareza/learnpython-day63-Working_With_Database_SQLLite/blob/master/resources/SQLAlchemyPycharmLibrary.png?raw=true)




