# Guesing game
secret_number = 8
guess_count = 0
guess_limit = 3             #The user has only three chances 

while guess_count < guess_limit:
    guess_number = int(input('Guess: '))
    guess_count += 1                     #incrementing the number of count 
    if guess_number == secret_number:      
       print('You won!')
       break
    elif guess_count < guess_limit: 
      print('Wrong guess, Guess again')
else:
 print('Oops! your out of guess')

