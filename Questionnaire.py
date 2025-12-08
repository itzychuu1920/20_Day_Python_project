questions = ("What is the largest mammal on Earth?",
             "Which planet is known as the \"Red Planet\"?",
             "In which city is the Brandenburg Gate located?",
             "How many colors are in a standard rainbow?",
             "What is the fear of insects called?",
             "Where was the first example of paper money used?",
             "Who invented the first practical automobile (motor car)?",
             )
options = (("A. Elephant", "B. BlueWhale", "C. Giraffe", "D. Hippopotamus"), 
           ("A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"), 
           ("A. Vienna", "B. Berlin", "C. Prague", "D. Zurich"), 
           ("A. Five", "B. Six", "C. Seven", "D. Eight"), 
           ("A. Arachnophobia", "B. Entomophobia", "C. Ailurophobia", "D. Claustrophobia"), 
           ("A. Greece", "B. Turkey", "C. China", "D. Egypt"), 
           ("A. Henry Ford", "B. Karl Benz", "C. Thomas Edison", "D. Nikola Tesla"))
answers = ("B", "C", "B", "C", "B", "C", "B")
guesses = []
score = 0
guess = "E"
question_num = 0
for question in questions:
    print("---------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"Answer is: {answers[question_num]}")
    question_num += 1
    print(f"Total Score is: {score}")
    print("Answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()
    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()