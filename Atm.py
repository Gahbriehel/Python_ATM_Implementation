from Account import Account


class Atm:
    # def __init__(self):
    pass


acc_no = int(input("Enter your Account number: "))
pin = int(input("Enter your PIN: "))
default_balance = 0
user = Account(acc_no, pin, default_balance)
while True:
    try:

        print("1. Withdrawal ")
        print("2. Deposit ")
        print("3. Balance Inquiry ")
        print("4. Buy Airtime ")
        choice = int(input("Select an option: "))
        if choice == 0:
            raise ValueError()
        if choice == 1:
            user.withdrawal()
        if choice == 2:
            user.deposit()
        if choice == 3:
            user.check_balance()
        if choice == 4:
            user.airtime_purchase()

    except ValueError:
        print("You need to Enter a valid number ")
    except TypeError:
        print("You need to Enter a number ")



