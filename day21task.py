a = ["Obi-Wan", "Anakin", "Ahsoka"]
b = ["Qui-gon", "windu", "yoda"]

print("List 1 :",a)

print("List 2 :",b)

x = list(map(tuple,zip(a, b)))

print("Merged list of tuples :",x)

range1 = range(1,9)

list1=[8,7,6,5,4,3,2,1]

print("Created range from 1 to 8 :",end=" ")

for i in range1:
    print(i,end=" ")

print("\nGiven list :",list1)

mergedList = list(map(tuple,zip(range1,list1)))

print("Merged list of tuples with range and given list :",mergedList)

list2=[8,3,9,7,1,2,4,6,5]

print("The given List : ",list2)

list3=sorted(list2)

print("The Sorted List :",list3)

def filterEven(n):
    if(n%2==0):
        return False
    else:
        return True

list4=[12,33,46,24,89,76,67,98,55]

print("Given List :",list4)

list5=list(filter(filterEven,list4))

print("After using the filter function that filter even numbers and with only odd numbers passed :",list5)
