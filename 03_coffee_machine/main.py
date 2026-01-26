from resources import current_resource, coffees

def is_resource_sufficient(current_resource, make_resource):
    if current_resource["water"] >= make_resource["water"] and current_resource["milk"] >= make_resource["milk"] and current_resource["coffee"] >= make_resource["coffee"]:
        return True
    return False

def update_resources(current_resource, make_resource):
    current_resource["water"] = current_resource["water"] - make_resource["water"] 
    current_resource["milk"] = current_resource["milk"] - make_resource["milk"] 
    current_resource["coffee"] = current_resource["coffee"] - make_resource["coffee"] 
    current_resource["money"] = current_resource["money"] + make_resource["money"]
    return current_resource

def find_coffee(coffee_name):
    for c in coffees:
        if c["name"] == coffee_name:
            return c
        
def print_resource_report():
    print(f"Water: {current_resource['water']}ml")
    print(f"Milk: {current_resource['milk']}ml")
    print(f"Coffee: {current_resource['coffee']}g")
    print(f"Money: ${current_resource['money']}")
    
    
print("Coffee Machine Design!!")
while True:
    chosen_drink = input("What would you like? espresso/latte/cappucino?: ").lower()
    
    if chosen_drink == "off":
        break

    if chosen_drink == "report":
        print_resource_report()
        continue

    selected_drink = find_coffee(chosen_drink)
    if not selected_drink:
        print("Invalid operation. Try again.")
        continue

    money = selected_drink["money"]
    
    if is_resource_sufficient(current_resource, selected_drink):
        coins = input("Please insert coins.")
        quaters = int(input("How many quaters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        dollar_conversion = (quaters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01)
        
        if dollar_conversion >= money:
            change_to_be_given = round((dollar_conversion - money), 2)
            if change_to_be_given > 0:
                print(f"Here is the ${change_to_be_given} change")

            final_resources_report = update_resources(current_resource, selected_drink)
            print(f"Here is your {chosen_drink} enjoy!")
            continue
        else:
            print("Sorry, thats not enough money. Money refunded")
            continue
    else:
        print("Sorry there is not enough resource")
        continue
        
    
