def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True
    print("Banking Program")
    while is_running:
        print("1. Show Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Enter Your Choice (1 - 4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice")
    print("Thank you. Have a nice day!")

if __name__ == '__main__':
    main()