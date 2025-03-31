class ATM():
    def __init__(self):
        self.balance = 0
    def display_menu(self):
        print("/nATM Menu")
        print("1. Credit")
        print("2. Debit")
        print("3. Balance")
        print("4. Exit")
    def get_choice(self):
        return input("Enter your choice (1-4): ")
    def credit(self):
        amount = float(input("Enter amount to credit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        else:
            self.balance += amount
            print(f"${amount} credited to your account.")    
    def debit(self):
        amount = float(input("Enter amount to debit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} debit from your account.")
    def show_balance(self):
        print(f"your current balance is: ${self.balance}")
    def run(self):
        while True:
            self.display_menu()
            choice = self.get_choice()
            if choice == '1':
                self.credit()
            elif choice == '2':
                self.debit()
            elif choice =='3':
                self.show_balance()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invaild choice. Please try again.")
atm = ATM()
atm.run()                
                            


            