print('1.Python script to merge two Python dictionaries')
dict1={1:'one',2:'two',3:'three'}
dict2={4:'four',5:'five'}
print('Dict1 : ',dict1)
print('Dict2 : ',dict2)
dict1.update(dict2)
print('Merged Dictonary : ',dict1)
print('2.program to sort the value from descending to ascending in list and convert it in to a set')
list1=[5,4,3,2,1]
print('list1 : ',list1)
list1.sort()
print('sorted list1 : ',list1)
set1=set(list1)
print('list1 after converting to set : ',set1)
print('3.Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function')
dict3={'key':[5,4,3,2,1]}
print('dict3 : ',dict3)
dict3['key'].sort()
print('dict3 after sorting its items with function : ',dict3)
dict4={'key':[5,4,3,2,1]}
print('sorting the items without using the function')
for i in range(len(dict4['key'])):
    for j in range(i + 1, len(dict4['key'])):
        if dict4['key'][i] > dict4['key'][j]:
           dict4['key'][i], dict4['key'][j] = dict4['key'][j], dict4['key'][i]
print('dict4 after sorting its items without function : ',dict4)
print('4.Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.')
str1='what is my name'
print('str1 : ',str1)
str2=input('Enter your  name : ')
str3=str1.replace('what', str2)
print('After changing the first occurance of the string with user specified input : ',str3)
print('5.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter')
str4='hello there general kenobi, hello  !'
print('str4 : ',str4)
list2=str4.split()
str5=input('Enter the word that you want to capitalize : ')
str6=''
for i in list2:
    if i==str5:
        str6+=(i.capitalize()+' ')
        continue
    str6+=(i+' ')
print('After changing all the occurances of the word in str4 :',str6)
print('6.Python program to find the repeated items of a list')
list3=[1,1,3,6,3,9,0,3,1,9,2,6]
print('list3 : ',list3)
print('The repeated items are : ',end='')
list4=[]
for i in range(len(list3)):
    if list3.count(list3[i])>1 and list3[i] not in list4:
        list4.append(list3[i])
        print(list3[i],end=' ')
print()
print('7.Python program to check the sum of three elements and divided by a value which is given as an input by the user')
num1=int(input('Enter  number 1 : '))
num2=int(input('Enter  number 2 : '))
num3=int(input('Enter  number 3 : '))
val=int(input('Enter the divisor value : '))
print('After performning the operation : ',(num1+num2+num3)/val)
print('8.Python program to find the Mean,median,mode among three given numbers')
print('The three numbers ',num1,num2,num3)
print('Mean : ',(num1+num2+num3)/3)
list5=[num1,num2,num3]
list5.sort()
print('Median : ',list5[1])
for i in range(len(list5)):
    if list5.count(list5[i])>1:
        print('Mode : ',list5[i])
        break
print('9.Python program to swap cases of a given string')
str7='This Is The Way'
print('str7 : ',str7)
print('After swapping the cases : ',str7.swapcase())
print('10.program to convert an integer to binary & octa decimal')
num=32
print('num6 : ',num)
print('num6 in binary : ',bin(num))
print('num6 in octa decimal : ',oct(num))
