# ANIMAL QUIZ
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    max_attempts = 1
    while still_guessing and attempt < max_attempts:            
        if guess.lower() == answer.lower():
            print('Correct answer')
            score += 1
            still_guessing = False
        else:
            attempt +=1
            if attempt < max_attempts-1:
                guess = input('Sorry, wrong answer. Try again. ')
            elif attempt == max_attempts-1:
                guess = input('Sorry, wrong answer. You only get one more guess. ')
        if attempt == max_attempts:
            print('The correct answer is ' + answer)
        
score = 0
print('Guess the Animal!')

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
