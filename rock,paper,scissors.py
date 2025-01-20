# creating rock, paper, scissors.
import random
def r_p_c(you, opponent):
    if you == opponent:
        print(f"opponent choice is {opponent}")
        print("...............................")
        print(f"your choice is {you}")
        print("it's a tie")
    elif you == r and opponent == p or you == p and opponent == s or you == s and opponent == r:
        game_running = False        
        print(f"opponent choice is {opponent}")
        print("...............................")
        print(f"your choice is {you}")
        print("you win")
        
    else:
        print(f"opponent choice is {opponent}")
        print("...............................")
        print(f"your choice is {you}")
        print("you lose")
        
r = "rock"
p = "paper"
s = "scissors"
game_running = True

while game_running:
    player = input(f"Choose one in | {r} | {p} | {s}:")
    opponent = random.choice([r, p, s])
    r_p_c(player, opponent)
    if game_running == False:
        break