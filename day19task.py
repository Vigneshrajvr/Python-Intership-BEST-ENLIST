import xlrd
import cx_Oracle
try:
    loc = ("Day_19_TaskExcel.xlsx")

    con = cx_Oracle.connect("hr/hr@localhost")
    cur=con.cursor()
    print("Connected to DataBase")

    wb = xlrd.open_workbook(loc)

    sheet = wb.sheet_by_index(0)
    print("Printing the values of the Excel data base.....") 
    for i in range(sheet.nrows):
        print(sheet.row_values(i))

    cur.execute("create table studentdatabase(id number(5),name varchar(10),cgpa float(5),dept varchar(5),year number(2))")
    print("Student Database created!")
    print("Reading values from excel and adding it to the oracle database.....")
    rows=[]
    for i in range(sheet.nrows):
        temp=sheet.row_values(i)
        rows.append(temp)
    cur.executemany("insert into studentdatabase values(:1,:2,:3,:4,:5)",rows)
    print("Printing values from the oracle database....")
    cur.execute("select * from studentdatabase")
    data=cur.fetchall()
    for i in data:
        for j in i:
            print(j,end=" ")
        print()
    con.commit()
    con.close()
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
