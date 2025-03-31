class atm():
    def __init__(self):
        self.balance=0
    def info(self):
        print("ATM list")
        print("1.credit\n", "2.withdrawl\n", "3.balance_enquiry\n", "4.exit")
    def credit(self):
        amount=int(input("enter the amount to credit to account"))
        if amount<0:
            print("enter valid amount")
        else:
            self.balance+=amount
            print(f"{amount}/-credited to your account")
    def withdraw(self):
        amount=int(input("enter the amount to withdraw from your account"))
        if amount<=0:
            print("input the vaild numbers")
        elif amount>self.balance:
            print("insufficient amount")
        else:
            self.balance-=amount
            print(f"{amount}/-debited from your account")
    def balance_check(self):
        print(f"{self.balance}/-is in your account")
    def run(self):
        while True:
            self.info()
            choice=input("enter your choice in 1-4 :")
            if choice=='1':
                self.credit()
            elif choice=='2':
                self.withdraw()
            elif choice=='3':
                self.balance_check()
            elif choice=='4':
                print(".....thank you for using our atm....")
                break
            else:
                print("enter correct number")
atm=atm()
atm.run()        
