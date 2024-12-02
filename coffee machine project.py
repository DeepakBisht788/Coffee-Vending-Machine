menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}
print("Espresso cost:150\nLatte cost:250\nCappuccino cost:300")
def x(order):
    is_enough=True
    for i in order:
        if (order[i])>=(resources[i]):
            print(f"Sorry there is not enough {i}.")
            is_enough=False
    return is_enough

def process_coins():
    print("Please insert money.")
    total = int(input("Enter Payment: ₹"))
    return total

def transaction(money_received,cost_price):
    e=True
    if money_received >= cost_price:
        change = round(money_received - cost_price, 2)
        print(f"Here is ₹{change} in change.")
        global profit
        profit += cost_price
        return e
    else:
        print("Sorry that's not enough money. Money refunded.")
        e=False
        return e
def make_coffee(drink_name, order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name}. Enjoy!")


a=True
while a:
    ask=input("What would you like? (espresso/latte/cappuccino):").lower()
    if ask=="off":
        a=False
    elif ask=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        a=menu[ask]
        if x(a["ingredients"]):
            payment=process_coins()
            if transaction(payment,a["cost"]):
                make_coffee(ask,a["ingredients"])
            
            
