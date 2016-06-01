import random

weapons = [
'shuriken',
'katana',
'axe',
'morningstar',
'claymore',
'sai',
'rapier',
'shotgun',
'rifle',
'pistol',
'wakizashi'
]

while True:
    start = input("Press enter/return to start; press 'q' to quit.")
    if start.lower() == 'q':
        break

    answer = random.choice(weapons)
    bad_guesses = []
    good_guesses = []
    
    while len(bad_guesses) < 7 and len(good_guesses) != len(answer):
        for letter in answer:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')
        print(' ')
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print(' ')
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue
            
        if guess in answer:
            good_guesses.append(guess)
            if len(good_guesses) == len(set(answer)):
                print("You win! The word was {}!".format(answer))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("You didn't guess it! My secret word was {}!".format(answer))
        
        
		
	