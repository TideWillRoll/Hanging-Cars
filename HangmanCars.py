#Python program for Hangman with car brands
import random
from collections import Counter

someWords = ["Acura", "Aston Martin", "Audi", "Bentley", "BMW", "Bugatti", "Buick", "Chevy", "Chrysler", "Dodge", "Ferrari", "Fiat", "Ford", "Genesis", 
             "GMC", "Honda", "Hyundai", "Infiniti", "Jaguar", "Kia", "Koenigsegg", "Lamborghini", "Lexus", "Lotus", "Maserati", 
             "McLaren", "Mercedes", "Mitsubishi", "Nissan", "Pagani", "Pontiac", "Porsche", "Plymouth", "Renault", "Rolls Royce", "Saleen", "Shelby", 
             "Tesla", "Toyota", "VW", "W Motors"]

#randomly chooses a secret word from "someWords".
word = random.choice(someWords)

if __name__=='__main__':
    print("Guess the word! Hint: word is a car brand")
    for i in word:
        print('_', end='')
        #For printing the empty spaces for letters of the word
    print()
    
    playing = True
    # List for storing the letters guessed by the player
    letterGuessed=''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0: # Flag is updated when the word is correctly guessed.
            print()
            chances -= 1
            
            try:
                guess = str(input("Enter a letter to guess: "))
            except:
                print("Enter only a letter!")
                continue
            
            # Guess validation
            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter only one letter")
                continue
            elif guess in letterGuessed:
                print("You have already guessed that letter")
                continue
            
            # If letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess # The guessed letter is added as many times as it occurs
                    
            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end='')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif (Counter(letterGuessed) == Counter(word)):
                    # the game ends, even if chances remain
                    print("The word is ", end='')
                    print(word)
                    flag = 1
                    print("Congratulations, You won!")
                    break # To break out of the for loop
                    break # To break out of the while loop
                else:
                    print('_', end='')
                    
            # if user has used all chances
            if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
                print()
                print("You lost! Try again...")
                print("The word was {}".format(word))
    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()