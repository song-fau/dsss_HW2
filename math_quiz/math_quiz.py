import random


def get_randomnumber(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)#to return a random number  between min and max


def get_operator():
    """
    Get an operator 
    """
    return random.choice(['+', '-', '*'])#return a random operator in the list


def get_problemandanswer(num1, num2, operator):
    """
    Get problem and answer
    """
    problem = f"{num1} {operator} {num2}"  # a string to describe the problem
    if operator == '+': 
        answer = num1 + num2   #calculate and get answer if operator is "+""
    elif operator == '-': 
        answer = num1 - num2   #calculate and get answer if operator is "-"
    else: 
        answer = num1 * num2   #calculate and get answer if operator is "*"
    return problem, answer

def math_quiz():
    """
    Start the math quiz
    """
    score = 0   #the initial score
    question_num = 10  #the total number of question

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(question_num):
        num1 = get_randomnumber(1, 10); #get a random integer between 1 and 10
        num2 = get_randomnumber(1, 5);  #get a random integer between 1 and 5
        operator = get_operator()       #get a random operator 

        PROBLEM, ANSWER = get_problemandanswer(num1, num2, operator) #get problem and answer
        print(f"\nQuestion: {PROBLEM}")
         
        
        while True:
            user_input = input("Your answer: ") #input a answer
            try:  #check if your answer is a valid input
                useranswer =int(user_input)
                break
            except ValueError:
                print("This is not a valid number, please input again:")
    

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{question_num}")

if __name__ == "__main__":
    math_quiz()
