import random
import nltk


nltk.download('words')
from nltk.corpus import words


word_list = words.words()

def choose():
    return random.choice(word_list)

def jumble(word):
    return " ".join(random.sample(word, len(word)))

def thank(p1n, p2n, p1, p2):
    print(p1n, 'Your score is:', p1)
    print(p2n, 'Your score is:', p2)
    print('Thanks for playing')
    print('Have a nice day')

def play():
    p1name = input('Player 1, please enter your name: ')
    p2name = input('Player 2, please enter your name: ')
    pp1 = 0 
    pp2 = 0
    turn = 0

    while True:
        picked_word = choose()    
        qn = jumble(picked_word)
        print("\nJumbled word:", qn)
        
        if turn % 2 == 0:
            print(p1name, 'your turn.')
            ans = input('What is on my mind? ')
            
            if ans == picked_word:
                pp1 += 1
                print('Correct! Your score is:', pp1)
            else:
                print('Better luck next time, I thought:', picked_word)

            c = input('Press 1 to continue and 0 to quit: ')
            if c == '0':
                thank(p1name, p2name, pp1, pp2)
                break
        else:
            print(p2name, 'your turn.')
            ans = input('What is on my mind? ')
            
            if ans == picked_word:
                pp2 += 1
                print('Correct! Your score is:', pp2)
            else:
                print('Better luck next time, I thought:', picked_word)

            c = input('Press 1 to continue and 0 to quit: ')
            if c == '0':
                thank(p1name, p2name, pp1, pp2)
                break  

        turn += 1

play()
