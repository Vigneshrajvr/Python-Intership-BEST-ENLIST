from tkinter import *
from tkinter import ttk

window = Tk()

window.title("Registration Screen")

window.geometry('700x500')

window.configure(background = "lightblue");
label1=Label(window,text= "EMPLOYEE REGISTRATION FORM", font=("bold", 20)).grid(row=0,column=3)
EmployeeName = Label(window ,text = "Employee Name: ").grid(row = 1,column = 2)
Email = Label(window ,text = "Email Id : ").grid(row = 2,column = 2)
Mobile = Label(window ,text = "Phone Number : ").grid(row = 3,column = 2)

Employeename1 = Entry(window).grid(row = 1,column = 3)
Email1 = Entry(window).grid(row = 2,column = 3)
Mobile1 = Entry(window).grid(row = 3,column = 3)

gender = Label(window,text='Gender : ').grid(row=4,column=2)
var = IntVar()
R1 = Radiobutton(window, text="Male", variable=var, value=1,).grid(row=4,column=3)

R2 = Radiobutton(window, text="Female", variable=var, value=2,).grid(row=4,column=4)

R3 = Radiobutton(window, text="Others", variable=var, value=3,).grid(row=4,column=5)

SelectNationality = Label(window ,text = "Nationality : ").grid(row = 5,column = 2)
variable = StringVar(window)
variable.set('India') 

country = OptionMenu(window, variable,'India','America','Japan','Europe','Australia').grid(row=5,column=3)

LangKnown = Label(window ,text = "Languages Known : ").grid(row = 6,column = 2)
pythonCheck = Checkbutton(window,text='Python').grid(row=6,column=3)
cCheck = Checkbutton(window,text='C').grid(row=6,column=4)
cPlusPlusCheck = Checkbutton(window,text='C++').grid(row=6,column=5)
javaCheck = Checkbutton(window,text='Java').grid(row=6,column=6)

Domain = Label(window ,text = "Domain : ").grid(row = 7,column = 2)
DomainEntry = Entry(window).grid(row = 7,column = 3)
Skills = Label(window ,text = "Skills : ").grid(row = 8,column = 2)
SkillsTextBox = Text(window,width=20, height=3).grid(row=8,column=3)
yearsExp=Label(window ,text = "Years of experience : ").grid(row=9,column = 2)
yearsExpSpinBox = Spinbox(window, from_=0, to=50).grid(row=9,column=3)

SubmitButton=Button(window,text="Submit",bg="pink").grid(row=11,column=3)
window.mainloop()
