bank_running = None
balance = 0
password = " "
tries = 5
while password != "irewolede" and tries > 0:
    password =input("Enter your password:")
    if password != "irewolede":
        print("wrong password")
        tries -= 1
        if tries == 0:
            break
        bank_running == False

else:
    bank_running = True
    print("1 -- to get balance.")
    print("2 -- to make a deposit")
    print("3 -- to make a withdrawal.")
    print("4 -- to exit the app.")
    while bank_running:
        application  = input("enter 1 - 2 - 3 - 4:")
        if not application.isdigit():
            print("Invalid input")
            continue
        application = int(application)        
        if application == 1:
            print(f"balance is... ${balance: 1f}")
        elif application == 2:
            print("making a deposit....")
            deposit = int(input("Enter an amount:"))
            if deposit < 0:
                print("deposit can't be less than zero..")
                continue
            else:
                print(f"you deposited an amount of.... ${deposit: 1f}")
            balance += deposit
        elif application == 3:
            print("making a withdrawal....")
            withdraw = int(input("Enter an amount:"))
            if withdraw <= balance:
                print("withdrawal successful....")
                balance -= withdraw
                print(f"remaining balance....${balance}")
            elif withdraw > balance:
                print("insufficient funds....")
        elif application == 4:
            bank_running == False
            break
        else:
            print("invalid input")
            break
if password != "irewolede":
    print("you need to verify your account, or you are not the owner....")
else:
    print("Thanks for choosing a transaction with us")
        

