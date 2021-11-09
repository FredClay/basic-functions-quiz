# python3
# Author: Fred Clay
# Date: 05 November 2021



import random, time
import pyinputplus as pyip


def quiz_starter(choice):
    if choice == '+':
        j = addition_quiz(time_per_question, questions_per_quiz)
        return j
    elif choice == '-':
        j = subtraction_quiz(time_per_question, questions_per_quiz)
        return j
    elif choice == 'x':
        j = multiplication_quiz(time_per_question, questions_per_quiz)
        return j
    else:
        j = division_quiz(time_per_question, questions_per_quiz)
        return j


def addition_quiz(time_allowance, questions):
    score_in_this_quiz = 0
    for i in range(1, questions + 1):
        num1 = random.choice(range(100))
        num2 = random.choice(range(100))
        answer = num1 + num2

        q_prompt = f"Question {i}: {num1} + {num2} = \n"

        try:
            response = pyip.inputNum(prompt=q_prompt, timeout=time_allowance, limit=1)

        except pyip.TimeoutException:
            print("Out of time!\n")
        except pyip.RetryLimitException:
            print("Out of tries!\n")
        else:
            if response == answer:
                score_in_this_quiz += 1
                print('Correct!\n')
                time.sleep(1)
            else:
                print(f"Incorrect. Answer was {answer}.\n")
                time.sleep(1)

    print(f'Quiz finished with a score of {score_in_this_quiz}/{questions}.')
    return score_in_this_quiz


def subtraction_quiz(time_allowance, questions):
    score_in_this_quiz = 0
    for i in range(1, questions + 1):
        num1 = random.choice(range(101))
        num2 = random.choice(range(num1, num1+101))
        answer = num2 - num1

        q_prompt = f"Question {i}: {num2} - {num1} = \n"

        try:
            response = pyip.inputNum(prompt=q_prompt, timeout=time_allowance, limit=1)

        except pyip.TimeoutException:
            print("Out of time!\n")
        except pyip.RetryLimitException:
            print("Out of tries!\n")
        else:
            if response == answer:
                score_in_this_quiz += 1
                print('Correct!\n')
                time.sleep(1)
            else:
                print(f"Incorrect. Answer was {answer}.\n")
                time.sleep(1)

    print(f'Quiz finished with a score of {score_in_this_quiz}/{questions}.')
    return score_in_this_quiz


def multiplication_quiz(time_allowance, questions):
    score_in_this_quiz = 0
    for i in range(1, questions + 1):
        num1 = random.choice(range(15))
        num2 = random.choice(range(15))
        answer = num1 * num2

        q_prompt = f"Question {i}: {num1} * {num2} = \n"

        try:
            response = pyip.inputNum(prompt=q_prompt, timeout=time_allowance, limit=1)

        except pyip.TimeoutException:
            print("Out of time!\n")
        except pyip.RetryLimitException:
            print("Out of tries!\n")
        else:
            if response == answer:
                score_in_this_quiz += 1
                print('Correct!\n')
                time.sleep(1)
            else:
                print(f"Incorrect. Answer was {answer}.\n")
                time.sleep(1)

    print(f'Quiz finished with a score of {score_in_this_quiz}/{questions}.')
    return score_in_this_quiz


def division_quiz(time_allowance, questions):
    score_in_this_quiz = 0
    for i in range(1, questions + 1):
        num1 = random.choice(range(1, 16))
        num2 = num1 * random.choice(range(0, 16))
        answer = num2 / num1

        q_prompt = f"Question {i}: {num2} / {num1} = \n"

        try:
            response = pyip.inputNum(prompt=q_prompt, timeout=time_allowance, limit=1)

        except pyip.TimeoutException:
            print("Out of time!\n")
        except pyip.RetryLimitException:
            print("Out of tries!\n")
        else:
            if response == answer:
                score_in_this_quiz += 1
                print('Correct!\n')
                time.sleep(1)
            else:
                print(f"Incorrect. Answer was {int(answer)}\n.")
                time.sleep(1)

    print(f'Quiz finished with a score of {score_in_this_quiz}/{questions}.')
    return score_in_this_quiz


# Default Settings.
time_per_question = 10
questions_per_quiz = 10

# Initial score values.
score = 0
questions_attempted = 0


# Printed whenever the user inputs 'RULES'.
rules = f'Select which quiz you would like to do. Enter your answer for each question where prompted.\n' \
        f'You have a limit of {time_per_question} seconds to answer each ' \
        f'question. \nCorrect answers given after the time allowed is exceeded will result in a no score.\n' \
        f'To quit the program and receive your final' \
        f'score, enter "QUIT" when on the quiz select prompt.\n'


#___________________________________________________________________#


if __name__ == '__main__':

    # Initial greetings.
    print("Ready to put those maths skills to the test?")
    print('To see the rules, enter \'rules\' any time between quizzes.')
    quiz_choice_string = 'Select which quiz you would like to do (+|-|x|/)'
    choices = ['+', '-', 'x', '/', 'RULES', 'EDIT', 'QUIT']


    while True:
        print(quiz_choice_string)
        quiz_chosen = pyip.inputMenu(choices, lettered=True)
        if quiz_chosen == 'QUIT':
            break
        if quiz_chosen == 'RULES':
            print(rules)
            continue
        if quiz_chosen == 'EDIT':
            time_per_question = pyip.inputNum(prompt='How much time would you like per question? ', min=1)
            questions_per_quiz = pyip.inputNum(prompt='How many questions would you like per quiz? ', min=1)
            continue

        # Else, run chosen quiz.
        score_from_quiz = quiz_starter(quiz_chosen)
        score += score_from_quiz
        questions_attempted += questions_per_quiz
        print(f'\nTotal Score: {score}/{questions_attempted}.\n\n')


    print('\nThank you for playing.')
    print(f'Final score: {score}/{questions_attempted}.')


#_______________________________________________________#









