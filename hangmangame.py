import random
def guess___word():
    while True:
        word = random___word()
        guess_word = []
        chances = 5
        print("Welcome to Hangman!")
        print(show__word(word,guess_word))
        while True:
            guess=input("enter the character:")
            if len(guess) !=1:
             print("enter a single letter")
             continue
            if guess in guess_word:
                print("You've already guessed that letter.")
                continue
            guess_word.append(guess)
            if guess not in word:
                chances-=1
                print(f"wrong guess you have {chances} chances left") 
            show_word=show__word(word,guess_word)
            print(show_word)
            if "_" not in show_word:
                print("congrats you win!")
                break
            if chances==0:
                print(f"you are out of attempts the word is {word}")
                break
def show__word(word,guessed_word):
    show_word=""
    for word in word:
        if word in guessed_word:
            show_word+=word
        else :
            show_word+="_"
    return show_word
def random___word():
    words={'america','antartica','arizona','india','paris','london','australia'}
    return random.choice(list(words))
if __name__=="__main__":
 guess___word()
