menu = """
[d] Deposit
[w] Withdraw
[s] Statement
[u] Create user
[a] Create account
[q] Quit

=> """


def deposit(balance, statement):
    amount = float(input("Amount to deposit: "))

    if amount < 0.01:
        raise ValueError("Invalid amount")

    balance += amount
    msg = f"Deposit of R$ {amount:.2f} made. New balance: R$ {balance:.2f}"
    statement.append(msg)
    print(msg)
    return balance


def withdraw(*, balance, statement, limit, withdraw_count, WITHDRAW_LIMIT):
    amount = float(input("Amount to withdraw: "))

    if amount < 0.01:
        raise ValueError("Invalid amount")

    if amount > limit:
        raise ValueError("Amount surpasses limit")

    if withdraw_count >= WITHDRAW_LIMIT:
        raise ValueError("Withdraw limit exceeded")

    if amount > balance:
        raise ValueError("Insufficient funds")

    balance -= amount
    withdraw_count += 1
    msg = f"Withdraw of R$ {amount:.2f} made. New balance: R$ {balance:.2f}"
    statement.append(msg)
    print(msg)
    return balance, withdraw_count


def print_statement(balance, /, *, statement):
    for s in statement:
        print(s)
    print(f"Balance: R$ {balance:.2f}")


def create_user(users):
    cpf = input("CPF: ")
    for user in users:
        if user["CPF"] == cpf:
            raise Exception("An user with this CPF already exists.")
    new_user = {
        "CPF": cpf,
        "name": input("Name: "),
        "birth_date": input("Birth date (dd-mm-yyyy): "),
        "address": input("Address (street, n., neighborhood, city/state): "),
    }
    users.append(new_user)
    print("User created successfully:\n")
    for k, v in new_user.items():
        print(f"{k}: {v}")


def create_account(users, AG, account_index, accounts):
    cpf = input("CPF: ")
    for user in users:
        if user["CPF"] == cpf:
            new_account = {
                "Ag": AG,
                "Account number": account_index + 1,
                "User": user["name"],
                "CPF": cpf,
            }
            accounts.append(new_account)
            print("Account created successfully:\n")
            for key, value in new_account.items():
                print(f"{key}: {value}")
            return account_index + 1
    raise Exception("No user with this CPF found.")


def main():
    statement = []
    balance = 0

    limit_per_withdraw = 500
    withdraw_count = 0
    WITHDRAW_LIMIT = 3

    users = []
    accounts = []
    AG = "0001"
    account_index = 0

    while True:
        try:
            choice = input(menu).lower()

            if choice == "d":
                balance = deposit(balance, statement)
            elif choice == "w":
                balance, withdraw_count = withdraw(
                    balance=balance,
                    statement=statement,
                    limit=limit_per_withdraw,
                    withdraw_count=withdraw_count,
                    WITHDRAW_LIMIT=WITHDRAW_LIMIT,
                )
            elif choice == "s":
                print_statement(balance, statement=statement)
            elif choice == "u":
                create_user(users)
            elif choice == "a":
                account_index = create_account(users, AG, account_index, accounts)
            elif choice == "q":
                break
            else:
                print("Invalid operation, please try again.")
        except ValueError as e:
            if "could not convert string to float" in str(e):
                print("Error: Invalid amount")
                continue
            print("Error:", e)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
