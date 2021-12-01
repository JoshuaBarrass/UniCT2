
class Item:
    
    def __init__(self, name, desctiption, Category, price):
        self.name = name
        self.price = price
        self.desc = desctiption
        self.Category = Category
        
    def getName(self):
        return self.name

    def getCategory(self):
        return self.Category
    
    def setCategory(self, cat):
        self.Category = cat
        
    def getDescription(self):
        return self.desc
    
    def setDescription(self, desc):
        self.desc = desc
    
    def getPrice(self):
        return self.price
        
    def setPrice(self, price):
        self.price = price



def main():
    ItemList = []
    # run a menu
    # has analysis mode
    while True:
        print("1. Analysis \n2. Edit \n3. Exit")
        choice = int(input("choice => "))
        
        if choice == 1:
            analysisMode(ItemList)
        
        elif choice == 2:
            editMode(ItemList)
        
        else:
            break
        
    


def editMode(items: list):
    indexCount = 0
    print("1. Add \n2. Edit")
    choice0 = int(input("Enter Number Choice => "))
    
    if choice0 == 1:
        
        newName = input("Item Name \t=> ")
        
        newDesc = input("Item Description \t=> ")

        newCate = input("Item Category \t=> ")

        newPrice = input("Item Price \t=> ")
            
        newitem = Item(newName, newDesc, newCate, newPrice)
        
        items.append(newitem)
        return items
        
    else:
        #Have add items
        while True:
            print("Ref Number \t item name")
            for item in items:
                print(f"{indexCount} |\t {item.getName()}")
                indexCount += 1 
                
            choice = int(input("Enter Reference Number to edit => "))
            if choice < len(items) and choice > -1:
                item = items[choice]
                print(f"{item.getName()} \t {item.getDescription()} \t {item.getCategory()} \t {item.getPrice()}")
                
                print("1. Edit \n2. Delete")
                choice2 = int(input("Enter Number Choice => "))
                if choice2 == 1:
                    print(f"Item Name: {item.getName()}")
                    print(f"Prev Desc: {item.getDescription()}")
                    newDesc = input("Leave Blank To Keep Old One \n New Desc \t=> ")
                    
                    if newDesc == "":
                        newDesc = item.getDescription()
                    
                    print(f"Prev Category: {item.getCategory()}")
                    newCate = input("Leave Blank To Keep Old One \n New Category \t=> ")
                    
                    if newCate == "":
                        newCate = item.getCategory()
                    
                    print(f"Prev Price: {item.getDescripgetPrice()}")
                    newPrice = input("Leave Blank To Keep Old One \n New Price \t=> ")
                    
                    if newPrice == "":
                        newPrice = item.getPrice()
                        
                    newitem = Item(item.name, newDesc, newCate, newPrice)
                    
                    items[items.index(item)] = newitem
                    return items
                    
                    
                elif choice2 == 2:
                    items.remove(item)
                    return items
                        
                
                return items
            else:
                print("Error: Not A Number")
            

main()