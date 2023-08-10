menu = """
[d] Deposit
[w] Withdraw
[s] Statement
[q] Quit

=> """

balance = 0
limit = 500
statement = []
withdraw_count = 0
WITHDRAW_LIMIT = 3


def deposit(amount):
    try:
        amount = float(amount)
        if amount < 0.01:
            raise ValueError("Invalid amount")

        global statement
        global balance

        balance += amount
        msg = f"Deposit of R$ {amount:.2f} made. Balance: R$ {balance:.2f}"
        statement.append(msg)
        print(msg)
    except ValueError as e:
        if "could not convert string to float" in str(e):
            return print("Error: Invalid amount")
        print("Error:", e)
    except Exception:
        print("Error: Please try again.")


def withdraw(amount):
    try:
        amount = float(amount)
        if amount < 0.01:
            raise ValueError("Invalid amount")

        global limit
        if amount > limit:
            raise ValueError("Amount surpasses limit")

        global withdraw_count
        global WITHDRAW_LIMIT
        if withdraw_count >= WITHDRAW_LIMIT:
            raise ValueError("Withdraw limit exceeded")

        global balance
        if amount > balance:
            raise ValueError("Insufficient funds")

        global statement
        balance -= amount
        withdraw_count += 1
        msg = f"Withdraw of R$ {amount:.2f} made. Balance: R$ {balance:.2f}"
        statement.append(msg)
        print(msg)
    except ValueError as e:
        if "could not convert string to float" in str(e):
            return print("Error: Invalid amount")
        print("Error:", e)
    except Exception:
        print("Error: Please try again.")


if __name__ == "__main__":
    while True:
        choice = input(menu)

        if choice == "d":
            amount = input("Amount to deposit: ")
            deposit(amount)
        elif choice == "w":
            amount = input("Amount to withdraw: ")
            withdraw(amount)
        elif choice == "s":
            if len(statement) < 1:
                print(f"Balance: R$ {balance:.2f}")
                continue
            for s in statement:
                print(s)
        elif choice == "q":
            break
        else:
            print("Invalid operation, please try again.")
