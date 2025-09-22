from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()
ordering = True

while ordering:
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == "report":
        coffee_maker.report()
        money.report()
    elif order == "off":
        print("Shutting down...")
        ordering = False
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)







