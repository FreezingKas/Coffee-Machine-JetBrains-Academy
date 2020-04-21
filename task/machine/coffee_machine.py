class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.resources_absent = ""

    def printCoffee(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee_beans) + " of coffee beans")
        print(str(self.disposable_cups) + " of disposable cups")
        print("$" + str(self.money) + " of money\n")

    def haveResources(self, cafe_type):
        if cafe_type == "1":
            if self.water - 250 > 0:
                pass
            else:
                self.resources_absent = "Water"
                return False
            if self.coffee_beans - 16 > 0:
                pass
            else:
                self.resources_absent = "Coffee Beans"
                return False
            if self.disposable_cups - 1 > 0:
                pass
            else:
                self.resources_absent = "Cups"
                return False
            return True
        if cafe_type == "2":
            if self.water - 350 > 0:
                pass
            else:
                self.resources_absent = "Water"
                return False

            if self.milk - 75 > 0:
                pass
            else:
                self.resources_absent = "Milk"
                return False

            if self.coffee_beans - 20 > 0:
                pass
            else:
                self.resources_absent = "Coffee Beans"
                return False

            if self.disposable_cups - 1 > 0:
                pass
            else:
                self.resources_absent = "Cups"
                return False

            return True
        if cafe_type == "3":
            if self.water - 200 > 0:
                pass
            else:
                self.resources_absent = "Water"
                return False

            if self.milk - 100 > 0:
                pass
            else:
                self.resources_absent = "Milk"
                return False

            if self.coffee_beans - 12 > 0:
                pass
            else:
                self.resources_absent = "Coffee Beans"
                return False

            if self.disposable_cups - 1 > 0:
                pass
            else:
                self.resources_absent = "Cups"
                return False

        return True

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        cafe_type = str(input())
        if cafe_type == "1":

            if self.haveResources(cafe_type):
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.disposable_cups -= 1
            else:
                print("Sorry, not enough " + self.resources_absent + "!")

        elif cafe_type == "2":
            if self.haveResources(cafe_type):
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.disposable_cups -= 1
            else:
                print("Sorry, not enough " + self.resources_absent + "!")

        elif cafe_type == "3":

            if self.haveResources(cafe_type):
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.disposable_cups -= 1
            else:
                print("Sorry, not enough " + self.resources_absent + "!")
        elif cafe_type == "back":
            print()
            return
        print()

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups += int(input())
        print()

    def take(self):
        print("I gave you $" + str(self.money) + "\n")
        self.money = 0


def action():
    io = ""
    while io != "exit":
        print("Write action (buy, fill, take, remaining, exit):")
        io = str(input())
        print()
        if io == "buy":
            coffee.buy()
        elif io == "fill":
            coffee.fill()
        elif io == "take":
            coffee.take()
        elif io == "remaining":
            coffee.printCoffee()
        elif io == "exit":
            exit()
        else:
            print("Wrong parameter!\n")


if __name__ == '__main__':
    coffee = CoffeeMachine()
    action()
