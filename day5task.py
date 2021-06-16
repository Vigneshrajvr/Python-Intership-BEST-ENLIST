def addItem(no,b):
    pos=int(input('Enter the position in which element needs to be inserted : '))
    no.insert(pos,b)
    return no
def deleteItem(b):
    no.remove(b)
    return no
no=list()
n=int(input('Enter the N value : '))
print('Enter the values : ')
for i in range(n):
    a=int(input())
    no.append(a)
print('The list : ',no)
b=int(input('Enter the element to be inserted : '))
no=addItem(no,b)
print('The list after insertion : ',no)
b=int(input('Enter the element to be deleted : '))
no=deleteItem(b)
print('The list after deletion : ',no)
mini=min(no)
maxi=max(no)
print('Minimum element is : ',mini)
print('Maximum element is : ',maxi)
tup=(4,5,6,7,3)
print('The created Tuple is : ',tup)
print('The reversed Tuple is : ',tup[::-1])
tup1=list(tup)
print('Conversion of tuple to list : ',tup1)

