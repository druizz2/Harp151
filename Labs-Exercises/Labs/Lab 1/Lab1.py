import random

# resources used: https://www.learnbyexample.org/python-lambda-function/ | https://towardsdatascience.com/six-tricks-you-should-know-about-python-dictionary-41c86570d282 | https://www.geeksforgeeks.org/python-assign-values-to-initialized-dictionary-keys/ | https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string | https://stackoverflow.com/questions/160930/how-do-i-check-if-an-integer-is-even-or-odd | https://www.w3schools.com/python/ref_string_split.asp | https://www.w3schools.com/python/ref_string_strip.asp | https://codereview.stackexchange.com/questions/95997/simple-game-of-hangman

# Question 1

list_one = ["apple", "rice", "gargoyle", "pandas", "sheep", "raptor"]

def returnLongestWord(list):
    index = list[0]     # set the index variable equal to the first element of the list as a starting point
    for i in list:      # loop through the list
        if len(i) > len(index): # comparing the length of each element in the list to the index var. 
            index = i      # if TRUE, set i as the new index. will check this for each element until loop terminates. 
    return index 

returnLongestWord(list_one)

# Question 2

filename = "/Users/daniel/Documents/GitHub/Harp151/Labs-Exercises/Lab 1/sowpods.txt"

def shortestWordDictionary():
    f = open(filename, "r", encoding = "utf8")
    words = f.readlines()
    f.close() 
    wordsDict = {}
    for i in range(10):
        randomWords = random.choice(words).strip()
        valueLength = len(randomWords)
        wordsDict[randomWords] = valueLength
    print(wordsDict)
    
    shortestWord = min(wordsDict, key = lambda x: len(x))
    return shortestWord

shortestWordDictionary()        

# Question 3 

def oddEvenName():
    name = input("Enter your name: ")
    nameString = name.strip().split()
    if len(nameString) % 2 == 0:
        return True
    else:
        return False
oddEvenName()

# Question 4

class Entity:
    def __init__(self, name, hp=100, shield=20, level=1):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.level = level

    
    def attack(self, damage, enemyShield, enemyHealth):
        self.damage = damage
        self.enemyShield = enemyShield
        self.enemyHealth = enemyHealth

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

    def getHealth(self):
        return self.hp

    def heal(self):
        currentHealth = self.getHealth()
        self.hp = min(currentHealth + 25, 100)

class Swordsman(Entity):
    def __init__(self, name, hp=200, shield=50, level=1, weapon = "Sword"):
        super().__init__(name, hp, shield, level)
        self.weapon = weapon
    
    def attack(self, damage, enemyShield, enemyHealth):
        print( f'{self.name} swung a {self.weapon} at the enemy, dealing {abs(damage - (enemyShield + enemyHealth))} damage!')

class Mage(Entity):
    def __init__(self, name, hp=100, shield=50, level=1, weapon = "Spell Tome"):
        super().__init__(name, hp, shield, level)
        self.weapon = weapon

    def attack(self, damage, enemyShield, enemyHealth):
        print( f'{self.name} used their {self.weapon} to throw a fire ball at the enemy, dealing {abs(damage - (enemyShield + enemyHealth))} damage!')


# Question 5

class Hangman:
    
    def main(self):
        # pictures for each incorrect guess
        pictureHangman = (
                     """
                     -----
                     |   |
                     |   0
                     |
                     |
                     |
                     |
                     |
                     |
                     --------
                     """,
                     """
                     -----
                     |   |
                     |   0
                     | /-+-\ 
                     |   | 
                     |   | 
                     |
                     |
                     |
                     --------
                     """,
                     """
                     -----
    G                |   |
    A                |   0
    M                | /-+-\ 
    E                |   | 
                     |   | 
    O                |  | | 
    V                |  | | 
    E                |
    R                --------
                    """)
        gameState = True    # for while loop
        wordChoices = ["Snow", "Five", "Screen", "Watch", "Laptop", "Phone", "Road", "Mountain", "Tree", "Rain", "Steps", "Roof", "Fan"]    # random word choices
        randomWordChoice = random.choice(wordChoices)   # selects a random string element from the list
        incorrectLetterGuesses = 0  # counter variable; will increment as number of incorrect letter guessses increases
        
        while gameState:    
            guess = str(input("Type in a word: "))  # input for guess
            if guess == randomWordChoice:
                print("\nYou guessed the correct word!\n")
                inp = input("Would you like to play again? Y/N\n")  # input to see if player wants to play again 
                if inp == "Y":  
                    self.main() # if yes, call the function to start the game again
                else:
                    break   # if no, end game
    
            else: 
                incorrectLetterGuesses +=1  # increment counter variable
                if incorrectLetterGuesses == 3: # check to see if the user has gone through all three attempts
                    print(f"Incorrect! You've run out of attempts! The word is {randomWordChoice}.")    # if so, reveal word choice 
                    print(pictureHangman[2])    # print corresponding picture
                    break   # end game
                else:
                    print(f"Incorrect, try again! You have {3-incorrectLetterGuesses} attempts remaining!") # prints number of guesses remaining for user
                    print(pictureHangman[abs((len(pictureHangman)-2) - incorrectLetterGuesses)])    # prints corresponding picture depending on number of guesses left
              
                                              
o = Hangman()
o.main()

# Question 6
# Overall, I'd rate my confidence level between 6.5-7. I would say my biggest issue is that, at times, I am forgetful of certain concepts, details, etc. For example,
# on question 3 in this lab I had completely forgetten about the modulo operator. Because of that, I spent lots of time trying to figure out how to do the queston, until 
# I had remembered it. Similarly, I also at times forget specifc nuances about certain data structures in python. Additionally, I also (at times) forget about built-in methods/functions
# that python has for it's data structures (i.e for dictionaries .get, .keys, etc). I would say I am comfortable with OOP and it's concepts, as well as 
# things like conditionals, loops, input, recursion, etc. For next week, maybe I would like to review more complex implementations of using user input, potentially wokring with APIs,
# using more packages for building specific types of programs (i.e pygame for gamedev), or introducing web app dev with python. Also, maybe Dr. Gibson can review more complex ideas
# of  data structures (dictionaries, tuples, etc), how to manipulate them, and create a complex implementation of them in a program we make. Additionally,maybe Dr. Gibson can explore things like making simple 
# ML models using packages like sckitlearn. 