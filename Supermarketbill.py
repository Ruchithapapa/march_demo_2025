name = input("Enter your name:")
#list of items
lists = '''
Rice      Rs 25/kg
Oil       Rs 50/liter
Salt      Rs 20/kg
Dal       Rs 120/kg
Sugar     Rs 40/kg
Onion     Rs 30/kg
'''

#Declaration
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

# Rate for each item
items = {'rice':25, 'oil':50, 'salt':20, 'dal':120, 'sugar':40, 'onion':30}
while True:
    option = input("press 1 for list or 2 to exit: ")
    if option == '2':
        print("Thank you shopping")
        break
    elif option == '1':
        print(lists)
        
        while True:
            inp1 = input("to buy press 1 or press 2 to exit: ")
            if inp1 == '2':
                print("Thank you for shopping")
                break
            elif inp1 == '1':
                item = input("Choose your items: ").lower()
                while True:
                    quantity_input = input("Enter quantity: ")
                    if quantity_input.isdigit():  #Check if input is digit or not
                        quantity = int(quantity_input)
                        break
                    else:
                        print("please enter a vaild quantity.")
                if item in items:
                    price = quantity*items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available. sorry for the inconvenience.")
        if totalprice > 0:
            tax = (totalprice*12)/100
            finalamount = tax + totalprice
            print(25 * "=", "pythonlife supermarket", 25 * "=")
            print(28 * " ", "Hyderabad")
            print("Name:", name, 30 * " ")
            print(75 * "-")
            print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range (len(pricelist)):
                print(i, 13 * " ", ilist[i], 8 * " ", 'quantity', 8 * " ", qlist[i], 8 * " ", plist[i])
            print(75 * "-",)
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print(75 * "-",)
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print(75 * "-")
            print(50 * " ", 'Final amount:', 'Rs', finalamount)
            print(75 * "-",)
            print(20 * " ", "Thank you & Visit again")
            print(75 * "-")
