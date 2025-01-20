question_no = 0
user = []
count = 0

questions = ("What is the longest river on  Earth", 
            "What is the tallest mountain on Earth", 
            "Who holds the record for the fastest man on Earth", 
            "What is the largest river on the planet", 
            "What is the largest ocean on Earth", 
            "What is the largest desert on Earth")

options = (("A: River Benue", "B: River Mississippi", "C: River Nile", "D: River Irewolede"), 
           ("A: Mount Kilimanjaro", "B: Mount Zuma", "C: Mount Olumo", "D: Mount Everest"), 
           ("A: Irewolede", "B: Usain Bolt", "C: Justin Gatlin", "D: Ronaldo"), 
           ("A: River Benue", "B: River Mississippi", "C: River Nile", "D: River Irewolede"), 
           ("A: Pacific Ocean", "B: Atlantic Ocean", "C: India Ocean", "D: Artic Ocean"), 
           ("A: Atakama Desert", "B: Namib Desert", "C: Kalahari Desert", "D: Sahara Desert"))

answers = ["C", "D", "B", "B", "A", "D"]


for question in questions:
    print(question)
    for option in options[question_no]:
        print(option)
    user_answer = input("Choose an answer:").upper()
    user.append(user_answer)
    if user_answer == answers[question_no]:
        print(">>>>>>> CORRECT ANSWER >>>>>>>>")
        count +=1
    else:
        print(">>>>>>> WRONG ANSWER >>>>>>")
        print(f"The answer is {answers[question_no]}")
    question_no += 1


print(f"Answers: {" ".join(answers)}")
print("your choice:", " ".join(user))
score = 100/6 * count
print(">>>> TOTAL SCORE% >>>>")
print(f"Score is {round(score,0)}%")
print(">>>>>>>>>>>>>>>>>>>>")