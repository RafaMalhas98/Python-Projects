import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

object_menu = Menu()
object_coffee_maker = CoffeeMaker()
object_money_machine = MoneyMachine()

print("> reports")
print(f"> {object_menu.get_items()}")

is_to_stop = False
while not is_to_stop:
    user_option = input("Choose a option: ").lower()
    if user_option == "reports":
        print("")
        object_coffee_maker.report()
        object_money_machine.report()

    elif user_option == "off":
        is_to_stop = True
    else:
        coffee_option = object_menu.find_drink(order_name=user_option)
        if coffee_option is not None:
            coffee_cost = coffee_option.cost
            print(f"The {user_option} costs {coffee_cost}{object_money_machine.CURRENCY}")
            is_payment_valid = object_money_machine.make_payment(cost=coffee_cost)
            if is_payment_valid:
                has_enough_resources = object_coffee_maker.is_resource_sufficient(drink=coffee_option)
                if has_enough_resources:
                    object_coffee_maker.make_coffee(order=coffee_option)

