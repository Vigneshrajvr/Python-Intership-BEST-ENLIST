dc={1:'supes',2:'batsy',3:'flash'}
marvel={4:'tony',5:'cap',6:'hulk'}
print('DC = ',dc)
print('Marvel = ',marvel)
dc.update(marvel)
print('Heroes = ',dc)
dc.pop(3)
print('Heroes after removing key 3 = ',dc)
lista=[1,2,3,4,5]
listb=['anakin','obiwan','yoda','asoka','rex']
sw=dict()
print('lista : ',lista)
print('listb : ',listb)
for i in range(len(lista)):
    sw[lista[i]]=listb[i]
print('After conversion of two list into a sw dictionary : ',sw)
set1={1,2,3,4,5}
set2={2,3}
print('Set1 : ',set1)
print('Set2 : ',set2)
print('Length of the set1 : ',len(set1))
set3=set1.difference(set2)
print('After removing the intersection of  2nd set from  1st set',set3)
