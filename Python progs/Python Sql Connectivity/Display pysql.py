def display_all():
     #display the records from a table
     #field by field
     import pymysql
     # Open database connection
     #conn=pymysql.connect(host='localhost',user='root',password='',db='test')
     db = pymysql.connect("localhost","root","","test4")
     # prepare a cursor object using cursor() method
     try:
         c = db.cursor()
         sql='select * from student;'
         c.execute(sql)
         countrow=c.execute(sql)
         print("number of rows : ",countrow)
         #data=a.fetchone()
         data=c.fetchall()
         #print(data)
         print("=========================")
         print("Roll No     Name     Per ")
         print("=========================")
         for eachrow in data:
             r=eachrow[0]
             n=eachrow[1]
             p=eachrow[2]
             # Now print fetched result
             print(r,'      ',n,'    ',p)
         print("=========================")
     except:
         db.rollback()
     # disconnect from server
     db.close()
# function calling
display_all()
