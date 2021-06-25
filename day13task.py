import re

print('1.Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)')
a = input('Enter the string : ')
if(re.search('[a-z]', a) or re.search('[A-Z]', a) or re.search('[0-1]', a)):
    print('The given string contains the character set [a-z],[A-Z],[0-9]')
else:
     print('The given string does not contain the character set [a-z],[A-Z],[0-9]')

print('2.Python program that matches a word containing ab')
b = input('Enter the string : ')
if(re.findall('ab', b)):
    print('Match found with ab',re.findall('ab', b))
else:
    print('Match not found')

print('3.Python program to check for a number at the end of a word/sentence')

c=input('Enter the string : ')

if(re.findall('[0-9]$', c)):
    print('The given string ends with a number')
else:
    print('The given string does not ends with a number')

print('4.Python program to search the numbers (0-9) of length between 1 to 3 in a given string')
d=input('Enter the string : ')
x=[]
if(re.findall('[0-9][0-9][0-9]', d) or re.findall('[0-9][0-9]',d) or re.findall('[0-9]', d)):
    x+=([re.findall('[0-9][0-9][0-9]', d)] + [re.findall('[0-9][0-9]',d)] + [re.findall('[0-9]', d)])
    print('Contains digits of 1-3 length : ',x)
else:
    print('No 1-3 length numbers found numbers found')

print('5.Python program to match a string that contains only uppercase letters')

e=input('Enter the string : ')

if(re.findall('[A-Z]', e)):
    print('The given string contains uppercase letters : ',re.findall('[A-Z]', e))
else:
    print('The given string contains no upper case letters')
