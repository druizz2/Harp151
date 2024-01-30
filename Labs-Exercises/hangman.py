import random

class Hangman:
    hangmanDrawings = ['''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''', '''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']
    
    filename = "sowpods.txt"

    def create_and_display_board():
        letters = ["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        gameState = True
        wordChoices = ["Snow", "Five", "Screen", "Watch", "Laptop", "Phone", "Road", "Mountain", "Tree", "Rain", "Steps", "Roof", "Fan"]
        randomWordChoice = random.choice(wordChoices)
        print(randomWordChoice)
        gameCount = len(randomWordChoice)
        gameState = True
        incorrectLetterGuesses = 0
        correctLetterGuesses = 0  # place holder variable for actual 
        # Here the board needs to be created
        while gameState:
            guess = str(input("Type in a word: "))
            if guess == randomWordChoice:
                print("Your guessed the correct word!")
                    # Board completely fills 
            else: 
                for i in letters:
                        if i in randomWordChoice:
                             correctLetterGuesses += 1
                             if correctLetterGuesses == gameCount:
                                  print("You won!")
                                  gameState = False

                        else:
                            incorrectLetterGuesses += 1
                           
                            
                  
                    # Hangman gets drawn here
    create_and_display_board()    
# 

                    
    
    

    
