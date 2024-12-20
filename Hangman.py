import random

nineWrong = """
      -----
      |   |
      O   |
     /|\  |
     / \  |
          |
    =======
    """
eightWrong = """
      -----
      |   |
      O   |
     /|\  |
     /    |
          |
    =======
    """

sevenWrong = """
      -----
      |   |
      O   |
     /|\  |
          |
          |
    =======
    """
sixWrong = """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =======
    """
fiveWrong =  """
      -----
      |   |
      O   |
      |   |
          |
          |
    =======
    """

fourWrong =  """
      -----
      |   |
      O   |
          |
          |
          |
    =======
    """
threeWrong =  """
      -----
          |
          |
          |
          |
          |
    =======
    """

twoWrong =  """
          |
          |
          |
          |
          |
    =======
    """
oneWrong =  """
   
    =======
    """

words = ["apple", "banana", "cherry", "date", "elderberry", 
        "fig", "grape", "honeydew", "kiwi", "lemon", 
        "mango", "nectarine", "orange", "papaya", "quince", 
        "raspberry", "strawberry", "tangerine", "watermelon", "blueberry"
    ]
alphabet = [
        "a", "b", "c", "d", "e", 
        "f", "g", "h", "i", "j", 
        "k", "l", "m", "n", "o", 
        "p", "q", "r", "s", "t", 
        "u", "v", "w", "x", "y", "z"
    ]
def hangman():
    usedLetters = []
    hiddenWord = random.choice(words)
    wrong = 0
    game = True
    display = ["_"] * len(hiddenWord)

    print("Welcome to Hangman!")
    name = input("What is your name?: ")
    print(f"Hello {name}")
    print("Hangman!!!")

    while game and wrong < 10:
        print("Your word:")
        print(display)
        guess = input("Guess a letter: ").lower()
        if guess in usedLetters:
            print("You've already guessed that letter.")
            continue

        if guess not in alphabet or len(guess) != 1:
            print("Please enter a valid letter.")
            continue
        
        usedLetters.append(guess)

        if guess in hiddenWord:
            print(f'Good Guess!! The letter {guess} is in the word!')
            for i in range(len(hiddenWord)):
                if hiddenWord[i] == guess:
                    display[i] = guess;
            print(f"Used Letters: {usedLetters}")
        else:
            wrong += 1
            print("Uh oh, one step closer to the gallows") 
            if wrong == 1:
                print(oneWrong)
                print(f"Used Letters: {usedLetters}")
            elif wrong == 2:
                print(twoWrong)
                print(f"Used Letters: {usedLetters}")
            elif wrong ==3:
                print(threeWrong)
                print(f"Used Letters: {usedLetters}")
            elif wrong == 4:
                print(fourWrong)
                print(f"Used Letters: {usedLetters}")
            elif wrong == 5:
                print(fiveWrong)
                print(f"Used Letters: {usedLetters}")
            elif wrong == 6:
                print(sixWrong)
                print(f"Used Letters: {usedLetters}")
            elif wrong == 7:
                print(sevenWrong)
                print(f"Used Letters: {usedLetters}")
            elif wrong == 8:
                print(eightWrong)
                print(f"Used Letters: {usedLetters}")
            elif wrong == 9:
                print(nineWrong)
                print(f"Game over the word was {hiddenWord}")
                print(f"Used Letters: {usedLetters}")
                game = False
        if '_' not in  display:
            print(f"Congratulations! You've guessed the word: {hiddenWord}")
            game = False

 







#call the function    
hangman()