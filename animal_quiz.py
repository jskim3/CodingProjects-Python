# ANIMAL QUIZ
# This program is allows you to create a short quiz with as many questions
# as the you would like to include
#
# The functions check_guess() allows you to define the the maximum number of guesses within the function
#    check_guess(guess, answer)
#        guess: input from user
#        answer: must be added by creator
# 

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    #define the maximum number of allowed attempts
    max_attempts = 3
    while still_guessing and attempt < max_attempts:            
        if guess.lower() == answer.lower():
            print('Correct answer')
            score += 1
            still_guessing = False
        else:
            attempt +=1
            if attempt < max_attempts-1:
                guess = input('Sorry, wrong answer. Try again: ')
            elif attempt == max_attempts-1:
                guess = input('Sorry, wrong answer. You only get one more guess: ')
        if attempt == max_attempts:
            print('The correct answer is ' + answer)

# Define the quiz name
quiz_name = 'Guess the Animal!'
score = 0
print(quiz_name)

# Format to ask questions where question and answer are strings entered by the creator
# [variable] = input(question)
# check_guess([variable], answer) 

guess1 = input('Which bear lives at the North Pole?: ')
check_guess(guess1, 'polar bear')

guess2 = input('Which is the fastest land animal?: ')
check_guess(guess2, 'cheetah')

guess3 = input('Which is the largest animal?: ')
check_guess(guess3, 'blue whale')

guess4 = input('Which one of these is a fish? \n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n (Type A, B, C, or D): ')
check_guess(guess4, 'C')

print('Your score is ' + str(score))
