def check_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit(balance):
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Successfully deposited ")
    else:
        print("Invalid deposit amount")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        print("Successfully withdrew")
    elif amount > balance:
        print("Insufficient balance")
    else:
        print("Invalid withdrawal amount")
    return balance

def main():
    correct_username = "123"
    correct_password = "123"
    balance = 00  # Initial balance
    
    print("STATE BANK OF INDIA")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login success")
        print("Welcome",correct_username)

        while True:
            print("\nSelect a service:")
            print("1. Check bank balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                check_balance(balance)
            elif choice == '2':
                balance = deposit(balance)
            elif choice == '3':
                balance = withdraw(balance)
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")
    else:
        print("Login failed")

if __name__ == "__main__":
    main()
