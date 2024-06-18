class Account:
    def __init__(self, acct_no=1234567890, pin=1234, balance=0):
        self.acctNo = int(acct_no)
        self.pin = int(pin)
        self.balance = int(balance)

    def deposit(self):
        deposit_amount = int(input("Enter amount to deposit: "))
        print("You have successfully deposited the sum of", deposit_amount)
        self.balance += deposit_amount
        print("Your current balance is", self.balance)

    def withdrawal(self):
        withdrawal_amount = int(input("Enter amount to withdraw: "))
        if withdrawal_amount > self.balance:
            print("You cannot withdraw more than your balance.")
        else:
            self.balance -= withdrawal_amount
            print("You have successfully withdrawn the sum of", withdrawal_amount)
            print("Your available balance is", self.balance)

    def check_balance(self):
        print("Your available balance is", self.balance)

    def airtime_purchase(self):
        while True:
            try:
                print("1. Airtime (self) ")
                print("2. Airtime (others) ")
                print("9. Quit")

                choice = int(input("Select airtime purchase option: "))

                if choice == 1:
                    airtime_amount = int(input("Enter amount: "))
                    if airtime_amount > self.balance:
                        print(f"You don't have sufficient balance to purchase {airtime_amount} airtime")
                    else:
                        self.balance -= airtime_amount
                        print(f"You have successfully purchased {airtime_amount} airtime")
                if choice == 2:
                    airtime_contact = int(input("Input recipient phone number: "))
                    airtime_amount = int(input("Enter amount: "))
                    if airtime_amount > self.balance:
                        print(f"You don't have sufficient balance to purchase {airtime_amount} airtime")
                    else:
                        self.balance -= airtime_amount
                        validate_pin = int(input("Enter your 4digit pin: "))
                        if validate_pin == self.pin:
                            print(f"You have successfully purchased {airtime_amount} airtime for {airtime_contact}")
                        else:
                            print("Incorrect pin.")

                if choice == 9:
                    return False

                if choice != 1 or choice != 2 or choice != 9:
                    raise ValueError

            except ValueError:
                print("Invalid selection ")
            except TypeError:
                print("You need to Enter a number ")


Gabe = Account(9876543210, 4321, 2)
# Gabe.deposit()
# Gabe.withdrawal()
# Gabe.check_balance()
# Gabe.airtime_purchase()
