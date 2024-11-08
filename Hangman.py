import random

def movie():
    movies = ["spiderman","batman","superman","bunnyman"]
    return random.choice(movies)

def play():
    chance = 6
    word = movie()
    letters = []  
    word_length = len(word)

    print(f"The selected  word has {word_length} letters")
    
    while chance > 0  :
        
        Present = ''.join([letter if letter in letters else '_' for letter in word])
        print("The Word is : ", Present)
        
        if Present == word:  
            print("You won!")
            return
        
        guess = input("\n \n Enter your guess : ").lower()
        
        if len(guess) != 1: 
            print("Please enter only one letter.")
            continue
        if guess.isnumeric ==True:
            print("Please enter alphabets only")
            continue
        if guess in letters:
            print("You've already guessed that letter.")
            continue
        
        letters.append(guess)  
        
        if guess not in word:
            chance -= 1
            print(f"Incorrect guess! You have {chance} chances left.")
        else:
            print("Good Play !")

    print(f"You lost! The word was '{word}'.")

play()
