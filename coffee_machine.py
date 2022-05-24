import time

products = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

flag = True
profit = 0
rest = 0


def menu():
    print("\n\t\t---Menu---")
    print("\t\tEspresso - $1.5")
    print("\t\tLatte - $2.5")
    print("\t\tCappuccino - $3.0")
    print("\t\tResources")
    print("\t\tOff")
    print()


def waiting():
    for i in range(1, 5):
        print(f"{user_input_product.capitalize()} preparing" + str(i * "."))
        time.sleep(1)


while flag:
    menu()
    dict_cost = {}
    for key, value in products.items():
        dict_cost[key] = value["cost"]

    user_input_product = input("What would you like? ")

    if user_input_product.lower() in products.keys():
        user_input_money = int(input("Insert money: $"))

        if user_input_money >= dict_cost[user_input_product]:
            rest = user_input_money - dict_cost[user_input_product]
            profit += dict_cost[user_input_product]
            print("Your rest: $" + str(rest) + "\n")
            waiting()
            print(f"Here is you {user_input_product.capitalize()}. Enjoy!\n")
            flag = False

        else:
            print("You don't have enough money")

    elif user_input_product.lower() == 'off':
        print("Profit: $" + str(profit))
        print("Turned off")
        flag = False

    elif user_input_product.lower() == 'resources':
        for key, value in resources.items():
            print(str(key) + ": " + str(value))
        flag = False

    else:
        print("Sorry, we don't have that product!")
        flag = False



