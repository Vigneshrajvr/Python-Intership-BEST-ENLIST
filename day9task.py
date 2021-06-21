import math
list=[1,2,3,4,5]
print(list)
n=len(list)
for i in range(0,n):
    list[i]+=2
print('List after adding +2 to every element:',list)

print("Printing Pattern:")
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")

n=int(input("Enter no of elemnts:"))
a=0
b=1
fib=0
print("Fibonacci Series is:")
for i in range(0,n+1):
    fib+=a
    a=b
    b=fib
    print(fib)

n=int(input("Enter a number:"))
temp=n
sum=0
while(temp>0):
    b=temp%10
    sum+=b**3
    temp//=10
if(sum==n):
    print("Given no is an Armstrong number")
else:
    print("No it is not an armstrong number")

print("Multiplication tables of 9:")
for i in range(1,11):
    print("9 X %d = %d"%(i,9*i))

n=int(input("Enter an integer:"))
if(n>0):
    print("Given integer is positive")
elif(n<0):
    print("Given integer is negative")
else:
    print("Given integer is zero")

days=int(input("Enter Number of days:"))
age=days//365
print("Age is",age)

print(math.degrees(math.pi/4))
print(math.radians(60))
print("Sine function:",math.sin(math.pi/4))
print("Cosine function:",math.cos(math.pi/3))
print("Tangent function:",math.tan(math.pi/2))
print("Inverse of sine in radians:",math.asin(1))
print("Inverse of cosine in radians:",math.acos(0))
print("Inverse of Tangent in radians:",math.atan(1))


while True:
    ch=input("Enter Your Choice('+','-','*','/'):")
    if ch in ('+','-','*','/'):
        a=int(input("Enter first number:"))
        b=int(input("Enter Second number:"))
        if(ch=='+'):
            print(a,"+",b,'=',a+b)
        elif(ch=='-'):
            print(a,"-",b,"=",a-b)
        elif(ch=='*'):
            print(a,"*",b,"=",a*b)
        else:
            print(a,"/",b,"=",a/b)
        
    else:
        print("Invalid input")
        break
