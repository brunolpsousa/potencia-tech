menu = """

[d] Deposit
[w] Withdraw
[s] Statement
[q] Quit

=>"""

balance = 0
limit = 500
statement = ""
withdraw_count = 0
WITHDRAW_LIMIT = 3


while True:
    choice = input(menu)

    if choice == "d":
        amount = input("Amount to deposit: ")
    elif choice == "w":
        amount = input("Amount to withdraw: ")
    elif choice == "s":
        print("Extrato")
    elif choice == "q":
        break
    else:
        print("Invalid operation, please try again.")
