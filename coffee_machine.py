class CoffeeMachine:

    materials = ['water', 'milk', 'coffee beans', 'disposable cups', 'money']
    balance = [400, 540, 120, 9, 550]

    def __init__(self):
        self.espresso = [250, 0, 16, 1, 4]
        self.latte = [350, 75, 20, 1, 7]
        self.cappuccino = [200, 100, 12, 1, 6]

    def remaining(self):
        print("\nThe coffee machine has:")
        for i in range(4):
            print(self.balance[i], 'of', self.materials[i])
        print('$' + str(self.balance[4]) + " of money")

    def calculation(self, coffee):
        for i in range(4):
            if self.balance[i] < coffee[i]:
                print(f"Sorry, not enough {self.materials[i]}!")
                return
        print("I have enough resources, making you a coffee!")
        for x in range(4):
            self.balance[x] -= coffee[x]
        self.balance[4] += coffee[4]

    def buy(self):
        """Choosing a type of coffee"""
        menu = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if menu == 'back':
            return
        elif menu == '1':
            self.calculation(self.espresso)
        elif menu == '2':
            self.calculation(self.latte)
        elif menu == '3':
            self.calculation(self.cappuccino)

    def fill(self):
        print()
        for i in range(2):
            self.balance[i] += int(input(f"Write how many ml of {self.materials[i]} do you want to add:\n"))
        self.balance[2] += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.balance[3] += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print(f"\nI gave you ${self.balance[4]}")
        self.balance[4] = 0

    def coffee_machine(self, action):
        """Choosing an action"""
        while action != 'exit':
            if action == "buy":
                self.buy()
                action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
            elif action == "fill":
                self.fill()
                action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
            elif action == "take":
                self.take()
                action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
            elif action == "remaining":
                self.remaining()
                action = input("\nWrite action (buy, fill, take, remaining, exit):\n")


CoffeeMachine().coffee_machine(input("\nWrite action (buy, fill, take, remaining, exit):\n"))
