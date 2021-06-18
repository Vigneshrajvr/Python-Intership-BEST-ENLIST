def getinput():
    a=int(input("Enter first integer:"))
    b=int(input("Enter Second integer:"))
    print("Addition of two numbers is:",add(a,b))
    print("Subtraction of two numbers is:",sub(a,b))
    print("Division of two numbers is:",divi(a,b))
    print("Multiplication of two numbers is:",multipli(a,b))

    
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multipli(x,y):
    return x*y
def divi(x,y):
    return x/y

getinput()

def printdetails(pat,temp):
    print("Patient name:",pat)
    print("Patient temperature:",temp)
    
    
def covid(name,temperature=98):
    patientname=name
    finaltemp=temperature
    printdetails(patientname,finaltemp)

covid("vicky",98)
covid("ruby")
covid("gokul",94)
