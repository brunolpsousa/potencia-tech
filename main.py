menu = """
[d] Deposit
[w] Withdraw
[s] Statement
[q] Quit

=> """


def deposit(balance, amount, statement):
    amount = float(amount)
    if amount < 0.01:
        raise ValueError("Invalid amount")

    balance += amount
    msg = f"Deposit of R$ {amount:.2f} made. New balance: R$ {balance:.2f}"
    statement.append(msg)
    print(msg)
    return balance


def withdraw(amount):
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
    msg = f"Withdraw of R$ {amount:.2f} made. New balance: R$ {balance:.2f}"
    statement.append(msg)
    print(msg)


def main():
    balance = 0
    limit_per_withdraw = 500
    statement = []
    withdraw_count = 0
    WITHDRAW_LIMIT = 3

    while True:
        try:
            choice = input(menu).lower()

            if choice == "d":
                amount = input("Amount to deposit: ")
                balance = deposit(balance, amount, statement)
            elif choice == "w":
                amount = input("Amount to withdraw: ")
                withdraw(amount)
            elif choice == "s":
                for s in statement:
                    print(s)
                print(f"Balance: R$ {balance:.2f}")
            elif choice == "q":
                break
            else:
                print("Invalid operation, please try again.")
        except ValueError as e:
            if "could not convert string to float" in str(e):
                print("Error: Invalid amount")
                continue
            print("Error:", e)
        except Exception:
            print("Error: Please try again.")


if __name__ == "__main__":
    main()
