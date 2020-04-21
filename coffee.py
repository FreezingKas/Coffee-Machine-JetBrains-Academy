class CoffeeMachine:
    def __init__(self):
        self.water = 1200
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def printCoffee(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee_beans) + " of coffee beans")
        print(str(self.disposable_cups) + " of disposable cups")
        print(str(self.money) + " of money\n")

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        cafe_type = int(input())
        if cafe_type == 1:
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
        elif cafe_type == 2:
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
        elif cafe_type == 3:
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups += int(input())

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0


def action():
    print("Write action (buy, fill, take):")
    io = str(input())
    if io == "buy":
        coffee.buy()
    elif io == "fill":
        coffee.fill()
    elif io == "take":
        coffee.take()
    else:
        print("Wrong parameter!")


if __name__ == '__main__':
    coffee = CoffeeMachine()
    coffee.printCoffee()
    action()
    print()
    coffee.printCoffee()
