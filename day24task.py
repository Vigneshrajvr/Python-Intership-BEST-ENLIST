import json
import cx_Oracle
try:
    con = cx_Oracle.connect("hr/hr@localhost")
    cur=con.cursor()
    print("Connected to DataBase")
    json_data=[
         {'name':'Rubesh','age':25,'Permanent_staff':True,'salary':57000.00,'dept_desgn':'Developer'},
         {'name':'Assane','age':35,'Permanent_staff':False,'salary':60000.00,'dept_desgn':'ML Engineer'},
         {'name':'Gokul','age':32,'Permanent_staff':True,'salary':78000.00,'dept_desgn':'Web Designer'},
         {'name':'Vignesh','age':23,'Permanent_staff':True,'salary':85000.00,'dept_desgn':'Data Scientist'},
         {'name':'Lupin','age':21,'Permanent_staff':True,'salary':67000.00,'dept_desgn':'Manager'}
    ]
    cur.execute("create table employee(name varchar(15),age number(5),permanent_staff varchar(10), salary float(15), dept_and_desgn varchar(15))")
    print("Table Created")
    rows=[]
    for i in json_data:
        j=i.values()
        j=list(j)
        rows.append(j)
    cur.executemany("insert into employee values(:1,:2,:3,:4,:5)",rows)
    con.commit()
    print("Values inserted")
    cur.execute("select * from employee")
    print("Fetching data from table")
    DBData=cur.fetchall()
    for i in DBData:
        print(i)
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
con.close()    
