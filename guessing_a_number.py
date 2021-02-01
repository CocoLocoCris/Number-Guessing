from random import randint

random_number = randint(1, 10) # This function is inclusive. That means it includes 1 AND 10.

guesses_left = 5

print("Let us play a game...\n" + "Guess a number from 1 to 10.\n" + "You have 5 tries.\n")

# The following loop is suppose to first filter out anything other than an integer.
# Then check to see if the guess is within the range 1 - 10.
# If input meets that criteria then wrong guesses get deducted from guesses_left.

while guesses_left > 0:
    
    try:
        
        guess = int(input("Give it your best guess: "))
        
        if guess not in range(1, 11): # The range() function includes the first number but not the last one.
        
            print("\nHey I said 1 through 10!\n" + "Learn to count!\n")
            
        elif guess == random_number:
            
            print("You got it right!")
            break
        
        else:
            
            print("\nNope! Not it.")
            guesses_left -= 1
            print("Tries left: " + str(guesses_left) + "\n")
        
    except:
        
        print("\n\nOnly numbers are allowed!\n\n")
        
if guesses_left == 0:
    
    print("Game Over!\nYou Lost.\nThe correct answer was " + str(random_number) + ".\n")