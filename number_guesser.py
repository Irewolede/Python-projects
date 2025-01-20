import random
def number_guess(x):
    random_guess = random.randint(1 , x)
    game_running = True
    while game_running:
        user_input = int(input(f"guess a number from 1 to {x}:"))
        if not user_input.is_integer():
            print("input must be interger")
            continue
        elif user_input == random_guess:
            print("you have guessed correctly")
            game_running = False
        elif user_input != random_guess:
            if user_input > random_guess:
                print("guess too high")
            else:
                print("guess too low")
    print("have a nice day")
x = 10
number_guess(x)




# now  making the computer guess a number

def computer_guess(y,x):
    game_running = True
    while game_running:
        if x == y:
            print("an error occured")
            break
        computer_choice = random.randint(y, x)
        print(f"computer choice: {computer_choice}") 
        my_choice = input("enter c if choice is correct | h for too high | l for too low:")
        if not my_choice.isalpha:
            print("must be an alphabet")
            continue
        elif my_choice == "c":
            print("the computer guessed correctly")
            game_running = False
        elif my_choice == "h":
            x = computer_choice - 1
        elif my_choice == "l":
            y = computer_choice + 1
    print("have a nice day")

computer_guess(1, 10000)
