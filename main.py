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
        print(f"Deposit of {amount} made. New balance: {balance}")
    except Exception:
        print("Error: please try again.")


while True:
    choice = input(menu)

    if choice == "d":
        amount = input("Amount to deposit: ")
        deposit(amount)
    elif choice == "w":
        amount = input("Amount to withdraw: ")
    elif choice == "s":
        print("Extrato")
    elif choice == "q":
        break
    else:
        print("Invalid operation, please try again.")
