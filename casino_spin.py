import random
import time
def spin():
    icon = ["💵","💶","💷","🤑","🧧"]
    return [random.choice(icon) for i in range(3)]

def bet_win(wheel, bet_amount):
    if wheel[0] == wheel[1] == wheel[2] and wheel[0] == "💵":
        return (bet_amount * 10)
    elif wheel[0] == wheel[1] == wheel[2] and wheel[0] == "💶":
        return (bet_amount * 8)
    elif wheel[0] == wheel[1] == wheel[2] and wheel[0] == "💷":
        return (bet_amount * 6)
    elif  wheel[0] == wheel[1] == wheel[2] and wheel[0] == "🤑":
        return (bet_amount * 4)
    elif wheel[0] == wheel[1] == wheel[2] and wheel[0] == "🧧":
        return (bet_amount * 2)
    return 0


balance = input("enter your balance:")
if not balance.isdigit():
    raise Exception ("Balance must be in digit")
else:
    balance = int(balance)
    if balance <= 0:
        print("balance can't be less than or equal to 0")
    else:
        print(f"Your balance is ${balance}")
        game_running = True


        while game_running:
            bet_spin = input("do you want to make a spin| yes or no:").lower()
            if bet_spin == "no":
                game_running = False
            elif bet_spin == "yes":
                bet_amount = int(input("Enter the amount you want to stake:"))
                if bet_amount > balance:
                    print("You don't have sufficient funds")
                    game_running = False
                else:
                    balance -= bet_amount
                    print(">>>>>> SPINNING WHEEL >>>>>>")
                    time.sleep(0.5)
                    wheel = spin()
                    print(" ".join(wheel))
                    my_win = bet_win(wheel, bet_amount)
                    if my_win > bet_amount:
                        print(f"you win ${my_win}")
                    else:
                        print(f"you lose ${bet_amount - my_win}")
                    balance += my_win
                    print(f"remaining balance is {balance}")


