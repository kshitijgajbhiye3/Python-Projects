questions = ("Capital City of India?",
             "Capital City of Maharashtra?",
             "Red Planet in our solar syatem?",
             "Who is the President of India?")

options = (("A. Mumbai","B. New Delhi","C. Delhi","D. Kolkata"),
           ("A. Mumbai","B. Nagpur","C. Pune","D. Nashik"),
           ("A. Earth","B. Mars","C. Venus","D. Jupiter"),
           ("A. Rahul Gandhi","B. Draupadi Murmu","C. Amit Shah","D. Narendra Modi"))

answers = ("B","A","B","D")

score = 0

user_ans = []

num = 0

for i in questions:
    print("______________________________")
    print(i)
    for j in options[num]:
        print(j)
    
    x = input("Enter your choice option: ").upper()
    user_ans.append(x)
    if x == answers[num]:
        score+=1
        print("Correct answer!")
    else :
        print("Wrong answer!")
        print(f"{answers[num]} is the right answer.")
    num+=1

print("Let's see the results..")
score = int(score / len(questions) * 100)
print(f"Your result is {score}%")