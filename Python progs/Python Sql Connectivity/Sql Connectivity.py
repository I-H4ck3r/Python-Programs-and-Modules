def insert_data():
     #take input for the details and then save the record in the databse
     #to insert data into the existing table in an existing database
     import pymysql
     # Open database connection
     #conn=pymysql.connect(host='localhost',user='root',password='',db='test')
     db = pymysql.connect("localhost","root","","test4")
     # prepare a cursor object using cursor() method
     c = db.cursor()
     r=int(input("Enter roll no "))
     n=input("Enter name ")
     p=int(input("Enter per "))
     try:
         # execute SQL query using execute() method.
         c.execute("insert into student (roll,name,per) values (%s,%s,%s)",(r,n,p))
         #to save the data
         db.commit()
         print("Record saved")
     except:
         db.rollback()
         # disconnect from server
     db.close()
# function calling
 insert_data()
