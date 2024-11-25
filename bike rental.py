class Bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displaystock(self):
        print("total no.of bike stock is ",self.stock)
    def rentforbike(self,quantity):
        if quantity <= 0:
            print("enter the postive number or grater than 0")
        elif quantity > self.stock:
            print("enter valid number(less stock)")
        else:
            print("the rental bike price is",quantity*100)
            print("total bike in stokyard",self.stock-quantity)
while True:
    obj=Bikeshop(100)
    uc = int(input("""
1 display stock
2 rent a bike  
3 exit                                    
"""))
    if uc == 1:
        obj.displaystock()
    elif uc == 2:
        n = int(input("enter no.of bikes you want on rent ="))
        obj.rentforbike(n)
    else:
        break        
    

    
        