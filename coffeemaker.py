MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}

MENU["espresso"]["ingredients"]["milk"] = 0

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

next_customer = True
while next_customer:
    c = input("What would you like? espresso/latte/cappuccino:\n").lower()
    if c == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
        next_customer = True
    elif c == "off":
        print("Shutting down.")
        next_customer = False
    else:
        choice = c
        if choice in MENU:
            if resources["water"] < MENU[f"{choice}"]["ingredients"]["water"]:
                print(f"Sorry, we don't have enough water.")
                next_customer = True
            elif resources["milk"] < MENU[f"{choice}"]["ingredients"]["milk"]:
                print("Sorry, we don't have enough milk.")
                next_customer = True
            elif resources["coffee"] < MENU[f"{choice}"]["ingredients"]["coffee"]:
                print("Sorry, we don't have enough coffee.")
                next_customer = True
            else:
                print("Please insert coins.")
                q = int(input("How many quarters: "))
                d = int(input("How many dimes: "))
                n = int(input("How many nickles: "))
                p = int(input("How many pennies: "))

                total = quarters*q + dimes*d + nickles*n + pennies*p
                if total < MENU[f"{choice}"]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                    next_customer = True
                else:
                    if choice in MENU:
                        change = total - MENU[f"{choice}"]["cost"]
                        print("Here is $" + str(round(change, 2)) + " in change.")
                        profit += MENU[f"{choice}"]["cost"]
                        next_customer = False
                    
                
                    resources["water"]=resources["water"]-MENU[choice]["ingredients"]["water"] 
                    resources["milk"]=resources["milk"]-MENU[choice]["ingredients"]["milk"] 
                    resources["coffee"]=resources["coffee"]-MENU[choice]["ingredients"]["coffee"]
                    next_customer = True
                
                    print(f"Here is your {choice}. Enjoy!")