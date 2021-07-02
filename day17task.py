
import cx_Oracle
try:
    # connecting database with python
    con = cx_Oracle.connect('hr/hr@localhost')
  
    cursor=con.cursor() 
    cursor.execute("create table manager(id int,name varchar(20))")    
    # inserting values in manager table
    cursor.execute("insert into manager values(1,'Anakin Skywalker')")
    cursor.execute("insert into manager values(2,'Obiwan Kenobi')")
    cursor.execute("insert into manager values(3,'Ahsoka Tano')")

    print("Manager Table created successfully and values inserted")
   
    cursor.execute("create table student(id int,name varchar(15))")
    # inserting values into student table
    cursor.execute("insert into student values(4,'Starkiller')")
    cursor.execute("insert into student values(5,'Fulcrum')")
    cursor.execute("insert into student values(6,'Ezra Miller')")
    print("Student Table created successfully and values inserted")
    

    cursor.execute("create table employee(id int,name varchar(15))")
    print("Employee Table created successfully")
    # inserting values into employee table
    cursor.execute("insert into employee values(7,'Rex')")
    cursor.execute("insert into employee values(8,'Fives')")
    cursor.execute("insert into employee values(9,'Echo')")
    cursor.execute("insert into employee values(10,'Cody')")
    print("Values inserted into employee table successfully")

    #printing employee table using for loop
    print("Printing employee table using for loop.....")
    cursor.execute("select * from employee")
    rows=cursor.fetchall()
    j=0
    for i in rows:
        print("Row ",(j+1),": ",i)
        j+=1
    con.commit()
except cx_Oracle.DatabaseError as e:
    print("There is a problem ", e)
con.close()
