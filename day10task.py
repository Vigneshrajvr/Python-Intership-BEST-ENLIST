class Banking(object):
    def __init__(self,accno,balance,name):
        self.accno = accno
        self.balance = balance
        self.name = name
    
class Ecommerce(Banking):
    def __init__(self,accno,balance,name,products):
        self.products=products
        super().__init__(accno,balance,name)
    def sendCash(self,per1,per2,amt):
        per1.balance-=amt
        per2.balance+=amt
    def receiveCash(self,per1,per2,amt):
        per1.balance+=amt
        per2.balance-=amt
def getBuyerInstance(name,accno):
    p1=personList[0]
    for i in range(len(personList)):
        if(accno == personList[i].accno and name==personList[i].name):
            p1=personList[i]
    return p1

def getSellerInstance(name):
    p2=personList[0]
    for i in range(len(personList)):
        if personList[i].name == name :
            p2=personList[i]
    return p2

def uploadData(personList,n):
    for i in range(n):
        print('Enter the details of person ',(i+1),' : ')
        name=input('Enter the name of person : ')
        accno=int(input('Enter the account no : ')) 
        balance=float(input('Enter the balance : '))
        noOfProducts=int(input('Enter the number of Products : '))
        products={}
        for j in range(noOfProducts):
            key = input('Enter product name : ')
            value = float((input('Enter the product price : ')))
            products[key]=value
        personList.append(Ecommerce(accno, balance, name, products))

personList =[]

n=int(input('Enter the number of persons: '))

uploadData(personList, n)



while True:
    print('1.Buy a product \n2.Sell a product\n3.Break')
    ch=input('Enter Your choice : ')
    if ch=='1' :
        accno = input('Enter your accno : ')
        name = input('Enter your name : ')
        for i in range(len(personList)):
            print(personList[i].name,'products',personList[i].products)
        p1=getBuyerInstance(name,accno)
        print('Your Balance : ',p1.balance)
        name = input('Enter the name of the seller : ')
        product = input('Enter the product name you want to buy from them : ')
        p2=getSellerInstance(name)
        p1.sendCash(p1, p2, p2.products[product])
        print('Product Bought! your new balance : ',p1.balance)
    elif ch=='2' :
        accno = input('Enter your accno : ')
        name = input('Enter your name : ')
        for i in range(len(personList)):
            print(personList[i].name,'products',personList[i].products)
        p2=getBuyerInstance(name,accno)
        name = input('Enter the name of the buyer : ')
        product = input('Enter the product name they are asking from you : ')
        p1=getSellerInstance(name)
        print('Buyer Balance : ',p1.balance)
        p1.receiveCash(p2, p1, p2.products[product])
        print('Product Bought! Buyer new balance : ',p1.balance)
    else:
        break
        
