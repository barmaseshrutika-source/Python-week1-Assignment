balance = 1000
correct_pin = "1234"

def check_balance():
    print("Your balance is:", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposited successfully!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdraw successful!")
    else:
        print("Insufficient balance!")

pin = input("Enter your PIN: ")

if pin == correct_pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Choose option: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid option")
else:
    print("Wrong PIN")
