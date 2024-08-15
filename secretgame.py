import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while random_number != guess: 
        guess = int(input(f'Guess anumber between 1 and {x}: '))
        if guess < random_number: 
            print('Guess is too low. guess again')
        elif guess > random_number:
            print('Guess is too high. guess again')
        
    print(f'Yay, congrats. Number {random_number} is correct')
            

#  

def computer_guess(x):
    low = 1
    high = x
    feedback= ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too High(H), too Low (L), OR Correct(C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif  feedback == 'l':
            low = guess + 1
    print(f'Computer guessed number {guess} correctly')
    
computer_guess(100)