import cx_Oracle
try:
    con = cx_Oracle.connect("hr/hr@localhost")
    cur=con.cursor()
    print("Connected to DataBase")
    cur.execute("create table doctor(doctorId number(10),doctorName varchar(10),noOfPatients number(10))")
    print("Table created")
    n=int(input("Enter the no of records you want to insert : "))
    rows=[]
    for i in range(n):
        dId=int(input("Enter the Id of doctor : "))
        dName=input("Enter the name of doctor : ")
        noOfPat=int(input("Enter the no of patients visited : "))
        rows.append((dId,dName,noOfPat))
    cur.executemany("insert into doctor values(:1,:2,:3)",rows)
    con.commit()
    print("Values inserted")
    cur.execute("select doctorName from doctor where noOfPatients>5")
    doctorList=cur.fetchall()
    print("Doctors having more than 5 patients visited.....")
    for i in doctorList:
        for j in i:
            print(j)
    cur.execute("select doctorName from doctor where noOfPatients=0")
    doctorList=cur.fetchall()
    print("Doctors having 0 patient visit.....")
    for i in doctorList:
        for j in i:
            print(j)
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
con.close()
