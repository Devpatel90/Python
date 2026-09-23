try:
    menu = {
        "coffee": {
            "ingredients":{
                "water" : 100,
                "milk" : 50,
                "coffee" : 20
            },
            "cost" : 90
        },
        
        "tea" :{
            "ingredients":{
                "water" : 100,
                "milk" : 50,
                "tea" : 10
            },
            "cost" : 50
        },
        
        "burger" :{
            "ingredients":{
                "bun" : 2,
                "cheese" : 1,
                "patty" : 1,
            },
            "cost" : 150
        },
        
        "milkshake" :{
            "ingredients":{
                "milk" : 100,
                "icecream" : 50,
                "syrup" : 30,
                "sugar" : 20,
            },
            "cost" : 120
        }
        
    }

    resources = {
        "water" : 300,
        "milk" : 300,
        "coffee" : 200,
        "tea" : 200,
        "bun" : 10,
        "cheese" : 10,
        "patty" : 10,
        "icecream" : 200,
        "syrup" : 200,
        "sugar" : 200,
    }

    def show_menu(menu):
        
        print("Name\t\tCost")
        for item in menu:
            print(f"{item:<15} {menu[item]['cost']}")   

    def take_order(menu, userchoice):
        while True:
            try:    
                quantity = int(input(f"How many {userchoice} you would like to have? "))
                if quantity <= 0:
                    print("Quantity must be greater than 0")
                    continue
                    
                total = menu[userchoice]["cost"] * quantity

                print(f"Cost: ₹{menu[userchoice]['cost']}")
                print("Choice:", userchoice)
                print("Quantity:", quantity)
                
                return userchoice, quantity, total
            
            except ValueError:
                print("Enter Valid Number")
                
        # except Exception as e:
        #     print("Error: Take_order",e)
        
    def check_resources(menu, resources, userchoice, quantity):
        ingredients = menu[userchoice]["ingredients"]
        for ingredient in ingredients:
            required = ingredients[ingredient] * quantity

            if resources[ingredient] < required:
                print(f"Not enough {ingredient}")
                return False

        return True

    def update_resources(menu, resources, userchoice, quantity):

        ingredients = menu[userchoice]["ingredients"]

        for ingredient in ingredients:
            required = ingredients[ingredient] * quantity
            resources[ingredient] -= required

    def process_payment(total):
       
        while True:
             try:
                print(f"Your Total is:- ₹{total}")
                payment = int(input("Enter Money:- ₹"))
                
                if payment < total:
                    print("Insufficient money")
                    continue

                change = payment - total
                
                print(f"Change:- ₹{change}")

                return True
            
             except ValueError:
                print("Enter Valid Number")
            
    
    solditems = {}
    totalsales = 0

    def sales(solditems,totalsales,userchoice, quantity, total):
        if userchoice in solditems:
            solditems[userchoice] += quantity
        else:
            solditems[userchoice] = quantity

        totalsales += total

        return solditems, totalsales        
    
    def show_report(solditems, totalsales, resources):

        print("\n--------------- DEV'S CAFE REPORT ---------------")

        print("\nSALES")

        for item in menu:
            print(f"{item:<15}: {solditems.get(item, 0)}")

        print(f"\nTotal Items Sold: {sum(solditems.values())}")
        print(f"Total Money Earned: ₹{totalsales}")

        print("\nREMAINING RESOURCES")

        for resource in resources:
            print(f"{resource:<15}: {resources[resource]}")
        

    show_menu(menu)
    while True:

            userchoice = input("What would you like to have? ""(coffee - tea - burger - milkshake - exit):- ")

            if userchoice == "exit":
                break

            elif userchoice == "report":
                show_report(solditems, totalsales, resources)

            elif userchoice in menu:

                userchoice, quantity, total = take_order(menu, userchoice)

                if check_resources(menu, resources, userchoice, quantity):

                    if process_payment(total):

                        update_resources(menu, resources, userchoice, quantity)

                        solditems, totalsales = sales(solditems, totalsales, userchoice, quantity, total)

                        print("Order prepared successfully!")
                        print("Here is Your Order. Enjoy!")

                else:
                    print("Cannot make the order.")

            else:
                print("Invalid Choice. Please try again.")
            
            

except Exception as e:
    print("Error", e)
    
    
finally:
    print("Thank You Visit Again")