import cx_Oracle
try:
    con = cx_Oracle.connect("hr/hr@localhost")
    cur=con.cursor()
    print("Connected to the DataBase")
    cur.execute("create table Employee(id number(5),name varchar(10),salary float(10))")
    print("Table created")
    n=int(input("Enter the number of employees : "))
    rows=[]
    for i in range(n):
        print("Enter the details of employee ",(i+1),".....")
        empId=int(input("ID : "))
        empName=input("NAME : ")
        empSalary=input("SALARY : ")
        rows.append((empId,empName,empSalary))
    cur.executemany("insert into Employee values(:1,:2,:3)",rows)
    print("Values inserted successfuly")
    con.commit()
    cur.execute("select max(salary) result from Employee")
    print("MAXIMUM SALARY :",cur.fetchall()[0][0])
    cur.execute("select min(salary) result from Employee")
    print("MINIMUM SALARY :",cur.fetchall()[0][0])
    cur.execute("select count(salary) result from Employee")
    print("NO OF EMPLOYEES WORKING IN THE COMPANY :",cur.fetchall()[0][0])
    cur.execute("select substr(name,0,3) result from Employee")
    fname=cur.fetchall()
    print("Printing the first 3 characters of the first name from Employee table .....")
    for i in fname:
        for j in i:
            print(j)
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
con.close()
