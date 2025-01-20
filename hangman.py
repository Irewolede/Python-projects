import random

words = ["irewolede", "opeyemi", "tomisin", "adenike", "olaoluwa", "oluwabukola", "alexander"]

def word_choose(words):
    word = random.choice(words)
    return word

def hangman():
    valid_word = word_choose(words) 
    available_word = list(valid_word)
    used_words = set()
    life = 6

    while len(available_word) != 0 and life > 0:
        print( "Used words....."," ".join(used_words))
        print()
        word_list = [letter if letter in used_words else "-" for letter in available_word]
        print("show_words"," ".join(word_list))
        user_words = input("choose a word at random guess:").lower()
        if not user_words.isalpha():
            print("word must be an alphabet")
            continue
        elif user_words in used_words:
            print("you have already entered this word.")
            if user_words in available_word:
                available_word.remove(user_words)
            else:
                life -= 1
                print(f"wrong guess...{life} lives remaining")
                
        else:
            used_words.add(user_words)

    if life == 0:
        print("you died")
    else:
        print(f"you guessed all. remains {life} lives")
    


hangman()




