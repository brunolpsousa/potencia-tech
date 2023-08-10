menu = """
[d] Deposit
[w] Withdraw
[s] Statement
[q] Quit

=> """

balance = 0
limit = 500
statement = ""
withdraw_count = 0
WITHDRAW_LIMIT = 3


def deposit(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Invalid amount")
        global balance
        balance += amount
        print(
            f"Deposit of R$ {amount:.2f} made. " +
            f"New balance: R$ {balance:.2f}"
        )
    except ValueError as e:
        if 'could not convert string to float' in str(e):
            return print('Error: Invalid amount')
        print("Error:", e)
    except Exception:
        print("Error: Please try again.")


def withdraw(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Invalid amount")

        global limit
        if amount > limit:
            raise ValueError("Amount surpasses limit")

        global balance
        if amount > balance:
            raise ValueError("Insufficient funds")

        global withdraw_count
        global WITHDRAW_LIMIT
        if withdraw_count >= WITHDRAW_LIMIT:
            raise ValueError("Withdraw limit exceeded")

        global statement
        balance -= amount
        withdraw_count += 1
        print(
            f"Withdraw of R$ {amount:.2f} made. " +
            f"New balance: R$ {balance:.2f}"
        )
    except ValueError as e:
        if 'could not convert string to float' in str(e):
            return print('Error: Invalid amount')
        print("Error:", e)
    except Exception:
        print("Error: Please try again.")


while True:
    choice = input(menu)

    if choice == "d":
        amount = input("Amount to deposit: ")
        deposit(amount)
    elif choice == "w":
        amount = input("Amount to withdraw: ")
        withdraw(amount)
    elif choice == "s":
        print("Extrato")
    elif choice == "q":
        break
    else:
        print("Invalid operation, please try again.")
