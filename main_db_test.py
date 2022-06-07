from database import mydatabase

print("connect db")
mydb = mydatabase()
print("create table book ")
mydb.create_book()
print("insert data book")
mydb.insert_book()
print("done")