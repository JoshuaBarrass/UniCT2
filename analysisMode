def analysisMode(items: list):
    loop = True
    while loop == True:
        analysischoice = int(input("1. Expenditure by category \n2. Average expendture per item \n3. Total Expenditure \n4. Exit \n"))
        if analysischoice == 1:
            categorychoice = input("Choose a category: ")
            for item in items:
                if item.getCategory() == categorychoice:
                    return f"{item.getName()} \t {item.getDescription()} \t {item.getCategory()} \t {item.getPrice()}"
        elif analysischoice == 2:
            sum = 0
            average = 0
            chooseitem = input("Choose the item you want the average expenditure for: ")
            for item in items:
                if item == chooseitem:
                    count = 0
                    count += 1
                    sum += item.price()
                    average = sum / count
                    return f'The average price of the item is {average}'
        elif analysischoice == 3:
            totalexp = 0
            for item in items:
                totalexp += item.price
            return totalexp
        else:
            loop = False
