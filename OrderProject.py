# category   #product    #order  #customerdetails
# catID  catName catDescription
categories = [[0, 1, 2, 3, 4],
              ["Electric", "Fire", "Water", "Flying", "Grass"],
              [
                  "The Electric type is a type of Pokémon that have electricity-oriented powers, they possess electro-kinetic abilities,",
                  "Fire-type moves are based on attacks of fire itself, and most of them can leave the status Burn, fire types are also immune to being Burned",
                  "There are more Pokémon of this type than any other type due to the large number of marine creatures to base species from!",
                  "Pokémon of this type can fly, many of them live at high altitudes, even. Most of them are based on birds and insects.",
                  "Many Grass types are based on plants and fungi, not necessarily grass. Many Grass-type Pokémon also belong to the Plant Egg Group..."]]
# PokemonID,    PokemonName,    Price,  TypeID
products = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            ["Pikachu", "Jolteon", "Charmander", "Ninetales",
             "Blastoise", "Psyduck", "MagiKarp", "Zapdos", "Pidgey", "Bulbasaur"],
            [12, 15.99, 8.20, 25, 22, 13, 3.33, 54, 7, 10],
            [0, 0, 1, 1, 2, 2, 3, 3, 3, 4]]
# custID custEmail custPhonenumber Adress Location Country
customers = [[0], ["test@gmail.com"], [7526655430], ["Buckingham Palace"], ["London"], ["UK"], [100]]
# orderid   #prodid     #quantity   #totalprice             customerID      #status
orders = [[0, 1, 2], [0, 6, 5], [4, 1, 5], [48.00, 3.33, 65.00], [0, 0, 0], ["Delivered", "Shipping", "Shipping"]]

catid = len(categories[0])
productid = len(products[0])
customerid = len(customers[0])
orderid = len(orders[0])

adminDetails = {
    "user": "admin123",
    "password": "pass123",
}


def getProduct(productID):
    name = ""
    for x in products[0]:
        if (x == productID):
            index = products[0].index(x)
            name = products[1][index]
    return name


def getCategory(CategoryID):
    name = ""
    for x in categories[0]:
        if (x == CategoryID):
            index = categories[0].index(x)
            name = categories[1][index]
    return name


def insertCategory(catid, catname, catdescription):
    categories[0].append(catid)
    categories[1].append(catname)
    categories[2].append(catdescription)
    print("Successfully Inserted Category {} with ID: ".format(catname), catid)
    input("Press Enter to Continue...")


def insertProduct(productid, prodname, price, catid):
    products[0].append(productid)
    products[1].append(prodname)
    products[2].append(price)
    products[3].append(catid)
    print("Successfully Inserted product {} with ID: ".format(prodname), productid)
    input("Press Enter to Continue...")


def insertCustomerDetails(customerid, custemail, phonenumber, address, location, country):
    customers[0].append(customerid)
    customers[1].append(custemail)
    customers[2].append(phonenumber)
    customers[3].append(address)
    customers[4].append(location)
    customers[5].append(country)
    customers[6].append(10)
    print("Customer Successfully Registered with CustomerID: ", customerid)
    input("Press Enter to Continue...")


def placeOrder(orderid, productid, quantity, totalprice, customerid, status):
    orders[0].append(orderid)
    orders[1].append(productid)
    orders[2].append(quantity)
    orders[3].append(totalprice)
    orders[4].append(customerid)
    orders[5].append(status)
    print("Order Placed Successfully: OrderID: {} TotalPrice: {}".format(orderid, totalprice))
    input("Press Enter to Continue...")


def getCustomerFunds(customerid):
    for x in customers[0]:
        if customerid == x:
            index = customers[0].index(x)
            moneyAvailable = customers[6][index]
    return moneyAvailable


def reduceCustomerFunds(customerid, cost):
    for x in customers[0]:
        if customerid == x:
            index = customers[0].index(x)
            moneyAvailable = customers[6][index]
            customers[6][index] = moneyAvailable - cost
            remainingBalance = customers[6][index]
    return remainingBalance


def increeaseCustomerFunds(customerid, cost):
    for x in customers[0]:
        if customerid == x:
            index = customers[0].index(x)
            moneyAvailable = customers[6][index]
            customers[6][index] = moneyAvailable + cost
            remainingBalance = customers[6][index]
    return remainingBalance


def checkCustDetails(custid):
    for x in customers[0]:
        if (custid == x):
            return True
    return False


def ordersPlaced(customerid):
    start = 0
    for x in orders[4]:
        if customerid == x:
            index = orders[4].index(x, start)
            print("Order ID: ", orders[0][index], end="\t")
            print("Product Id: ", orders[1][index], end="\t")
            print("Product Name: ", getProduct(orders[1][index]), end="\t")
            print("Quantity: ", orders[2][index], end="\t")
            print("Total Price: ", orders[3][index], end="\t")
            print("CustomerID: ", orders[4][index], end="\t")
            print("Status: ", orders[5][index], end="\t")
            print("location: ", customers[4][customerid], end="\t")
            start = index + 1
            print()
    input("Press Enter to Continue...")


def printCustomerDetails(customerid):
    for x in customers[0]:
        if customerid == x:
            index = customers[0].index(x)
            print("Customer-ID: ", customers[0][index], end="\t")
            print("Email Address: ", customers[1][index], end="\t")
            print("Phone Number: ", customers[2][index], end="\t")
            print("Address: ", customers[3][index], end="\t")
            print("Location: ", customers[4][index], end="\t")
            print("Country: ", customers[5][index], end="\t")
            print("Wallet Funds: £:", customers[6][index], end="\t")
            print()
    input("Press Enter to Continue...")


def productSearch(CategoryID):
    l = []
    prices = []
    prodid = []
    start = 0
    for x in products[3]:
        if (x == CategoryID):
            index = products[3].index(x, start)
            l.append(products[1][index])
            prices.append(products[2][index])
            prodid.append(products[0][index])
            start = index + 1
    return l, prices, prodid


def checkAdminDetails(username, password):
    if username == adminDetails["user"] and password == adminDetails["password"]:
        return True
    else:
        return False


def adminProductSales(product_id, incall):
    # amount = orders[1].count(product_id) #chagne this
    Tprice = 0
    start = 0
    quantity = 0
    for x in orders[1]:
        if x == product_id:
            index = orders[1].index(x, start)
            Tprice = Tprice + orders[3][index]
            quantity = quantity + orders[2][index]
    index = products[0].index(product_id)
    price = products[2][index]
    total = Tprice
    product = getProduct(product_id)
    if (incall == False):
        print(
            "ProductID: {} | Product Name {} | Amount Sold {} | Product Price {:.2f} | Total Revenue(£) Made: {:.2f} ".format(
                product_id, product, quantity, price, total))
        input("Press Enter to Continue...")
    return total


def adminCategorySales(cat_id):
    total = 0
    start = 0
    for x in products[3]:
        if x == cat_id:
            index = products[3].index(x, start)
            prodid = products[0][index]
            total = total + adminProductSales(prodid, True)
            start = index + 1
    Categoryname = getCategory(cat_id)
    print("CategoryID: {} | Category Name: {} | Total Revenue made in Category: {:.2f}".format(cat_id, Categoryname,
                                                                                               total))
    input("Press Enter to Continue...")
    return total


def adminSalesOrdered(ascending):
    sales = []
    # details
    for x in orders[3]:
        sales.append(x)

    if ascending:
        sales.sort()
        return sales
    else:
        sales.sort(reverse=True)
        return sales


def getSalesOfCustID(custid):
    total = 0
    start = 0
    for x in orders[4]:
        if x == custid:
            index = orders[4].index(x, start)
            total = total + orders[3][index]
            start = index + 1
    return total


def adminSalesLocation(location):
    total = 0
    start = 0
    print("All Orders Created From {}:".format(location))
    for x in customers[4]:
        if x == location:
            index = customers[4].index(x, start)
            cust_id = customers[0][index]
            total = total + getSalesOfCustID(cust_id)
            ordersPlaced(cust_id)
            start = index + 1
    return total


# UI:
resume = True
while resume:
    print('─' * 25)
    print("Customer Menu:\n0:Quit\n1:Product Search\n2:Customer\n3:Admin\n4:Insert\n5:Register Customer ")
    print('─' * 25)
    option = int(input("Please Enter an Option: "))

    if (option == 0):
        print("Successfully quit...")
        break
    elif (option == 1):
        category_name = input("Please enter the Category that you want to search for: ")
        if (category_name in categories[1]):
            index = categories[1].index(category_name)
            CatId = categories[0][index]
            L, Price, prodIDS = productSearch(CatId)
            print("Products of Category {}:  ".format(category_name))
            for i in range(len(L)):
                print("Product:  ", L[i], " Price: ", Price[i])
            decision = int(input("Do you want to buy any of these products from this search? yes(1) no(0): "))
            if decision == 1:
                product = input("Please Specify The product to buy: ")
                if product in L:
                    quantity = int(input("How many of these Would you like to buy??"))
                    customerID = int(input("Enter Customer ID: "))
                    if checkCustDetails(customerID):
                        totalPrice = (Price[L.index(product)]) * quantity
                        fundsAvailable = getCustomerFunds(customerID)

                        if totalPrice <= fundsAvailable:
                            remainingBalance = reduceCustomerFunds(customerID, totalPrice)
                            productID = (prodIDS[L.index(product)])
                            status = "Shipping"
                            print("Your remaining balance: £{}".format(remainingBalance))
                            placeOrder(orderid, productID, quantity, totalPrice, customerID, status)
                            orderid = orderid + 1

                        else:
                            print("You do not have enough funds...")
                else:
                    print("Product is not there...")
            elif decision == 0:
                print("Understandable...")
            else:
                print("Wrong option inputted")
        else:
            print("Category doesn't exist or there are no products underneath this category...")

    elif (option == 2):
        customerID = int(input("Enter Customer ID: "))
        if (checkCustDetails(customerID) == True):
            print("\033[1;32;40m" + "Correct CustomerID!!!" + "\033[0m")
            print('─' * 25)
            print("0:View Orders Placed \n1:View Your Details\n2:Add Funds To Wallet")
            decision = int(input("Please Select an Option: "))
            if (decision == 0):
                ordersPlaced(customerID)
            elif (decision == 1):
                printCustomerDetails(customerID)
            elif (decision == 2):
                funds = int(input("How much £ would you like to add: "))
                remainingBalance = increeaseCustomerFunds(customerID, funds)
                print("Funds Added Successfully your balance is now: £{}".format(remainingBalance))
            else:
                print("invalid option entered")
        else:
            print("You have Entered an invalid Customer ID")

    elif (option == 3):
        valid = False
        while valid == False:
            username = input("Enter your User-Name: ")
            password = input("Enter your Password: ")
            if (checkAdminDetails(username, password) == True):
                valid = True
                print("\033[1;32;40m" + "Admin Login Successful!!" + "\033[0m")
                adminMenu = True
                while adminMenu:
                    print('─' * 25)
                    print(
                        "Admin Menu:\n0:Orders By ProductID\n1:Orders by Category\n2:Orders By Location\n3:Total Orders By Price\n4:Quit ")
                    print('─' * 25)
                    decision = int(input("Please Enter an Option: "))
                    if decision == 0:
                        ProductID = int(input("Please Enter a Product ID: "))
                        if (ProductID not in products[0]):
                            print("Product Doesn't Exist")
                        else:
                            adminProductSales(ProductID, False)
                    elif decision == 1:
                        CategoryID = int(input("Please Enter a CategoryID to Search: "))
                        if (CategoryID not in categories[0]):
                            print("Category Doesn't Exist")
                        else:
                            adminCategorySales(CategoryID)
                    elif decision == 3:
                        print("0:Low to High\n1:High to Low")
                        AscDesc = int(input("Please Enter an Option: "))
                        if (AscDesc == 0):
                            L = adminSalesOrdered(True)
                            print("Log of all Order Sales (Low-> High)::")
                            count = 0
                            for x in L:
                                count = count + 1
                                print("Order: {} | Total Order Price: {}".format(count, x))
                            input("Press Enter to Continue...")
                        elif (AscDesc == 1):
                            L = adminSalesOrdered(False)
                            print("Log of all Order Sales (High-> Low)::")
                            count = 0
                            for x in L:
                                count = count + 1
                                print("Order {} | Order Price: {}".format(count, x))
                            input("Press Enter to Continue...")
                        else:
                            print("Invalid Option Entered")
                    elif decision == 2:
                        location = input("Enter Location to search from: ")
                        sales = adminSalesLocation(location)
                        print("Total £ made From Orders in {}: {:.2f}".format(location, sales))
                        input("Press Enter to Continue...")
                    elif decision == 4:
                        print("Quit Admin Successfully")
                        break
                    else:
                        print("Wrong Option Entered")

            else:
                valid = False
                print("\033[1;31;40m" + "Email or Password Incorrect Please Re-Enter" + "\033[0m")
    elif (option == 4):
        print("0:Add Category\n1:Add Product ")
        decision = int(input("Enter an Option: "))
        if (decision == 0):
            name = input("What is the name of the category? ")
            description = input("Please Enter a category Description: ")
            insertCategory(catid, name, description)
            catid += 1

        elif (decision == 1):
            name = input("Enter the product's name: ")
            price = float(input("Enter the product's price: "))
            categoryID = int(input("Enter the Category ID for the product: "))
            if (categoryID not in categories[0]):
                print("This Category does not exist")
            else:
                insertProduct(productid, name, price, categoryID)
                productid = productid + 1
        else:
            print("Invalid Input...")
    elif (option == 5):
        valid = False
        while not valid:
            email = input("Enter your email: ")
            l = email.split('@')
            if len(l) != 2:
                valid = False
            else:
                t = ('co', 'com', 'org', 'in')
                for x in t:
                    temp = l[1].split('.')
                    try:
                        if len(temp[0]) > 0 and temp[1] == x:
                            valid = True
                            break
                    except:
                        valid = False
                    else:
                        valid = False
        valid = False
        while not valid:
            number = int(input("Enter your number: "))
            number1 = str(number)
            if len(number1) == 10:
                valid = True

        address = input("Enter Address: ")
        location = input("Enter Location: ")
        country = input("Enter Country: ")

        insertCustomerDetails(customerid, email, number, address, location, country)
        customerid = customerid + 1

    else:
        print("invalid input..")
