print('1.Python script to merge two Python dictionaries')
dc={1:'supes',2:'bat',3:'flash'}
marv={4:'cap',5:'thor'}
print('Dc : ',dc)
print('Marvel : ',marv)
dc.update(marv)
print('Merged Dictonary Heroes: ',dc)
print('2.Program to sort the value from descending to ascending in list and convert it into a set')
a=[5,4,3,2,1]
print('list : ',a)
a.sort()
print('sorted list : ',a)
seta=set(a)
print('list after converting to set : ',seta)
print('3.Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function')
dict={'key':[9,8,7,6,5]}
print('dict : ',dict)
dict['key'].sort()
print('dict after sorting its items with function : ',dict)
dict1={'key':[5,4,3,2,1]}
print('sorting the items without using the function')
for i in range(len(dict1['key'])):
    for j in range(i + 1, len(dict1['key'])):
        if dict1['key'][i] > dict1['key'][j]:
           dict1['key'][i], dict1['key'][j] = dict1['key'][j], dict1['key'][i]
print('dict1 after sorting its items without function : ',dict1)
print('4.Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.')
str='countryname is my country'
print('string : ',str)
str1=input('Enter your country name : ')
str2=str.replace('countryname', str1)
print('After changing the first occurance of the string with user specified input : ',str2)
print('5.Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter')
string='the red car is nice and the car looks like bmw car'
print('string : ',string)
list2=string.split()
str5=input('Enter the word that you want to capitalize : ')
str6=''
for i in list2:
    if i==str5:
        str6+=(i.capitalize()+' ')
        continue
    str6+=(i+' ')
print('After changing all the occurances of the word in str4 :',str6)
print('6.Python program to find the repeated items of a list')
list3=[1,1,3,2,1,9,0,3,1,1,2,6]
print('list3 : ',list3)
print('The repeated items are : ',end='')
list4=[]
for i in range(len(list3)):
    if list3.count(list3[i])>1 and list3[i] not in list4:
        list4.append(list3[i])
        print(list3[i],end=' ')
print()
print('7.Python program to check the sum of three elements and divided by a value which is given as an input by the user')
num1=int(input('Enter the number 1 : '))
num2=int(input('Enter the number 2 : '))
num3=int(input('Enter the number 3 : '))
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
str7='Python Is My Favourite Language'
print('str7 : ',str7)
print('After swapping the cases : ',str7.swapcase())
print('10.program to convert an integer to binary & octa decimal')
num4=16
print('num6 : ',num4)
print('num6 in binary : ',bin(num4))
print('num6 in octa decimal : ',oct(num4))
