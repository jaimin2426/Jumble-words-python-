import random
import nltk

# Download words corpus if not already present
nltk.download('words')
from nltk.corpus import words

word_list = words.words()

def choose():
    return random.choice(word_list)

def jumble(word):
    return " ".join(random.sample(word, len(word)))

def thank(p1n, p2n, p1, p2):
    print("\nFinal Scores:")
    print(p1n, 'Your score is:', p1)
    print(p2n, 'Your score is:', p2)

    # Winner announcement
    if p1 > p2:
        print(f"🎉 {p1n} wins the game!")
    elif p2 > p1:
        print(f"🎉 {p2n} wins the game!")
    else:
        print("🤝 It's a tie!")

    print('Thanks for playing!')
    print('Have a nice day 😊')

def play():
    p1name = input('Player 1, please enter your name: ')
    p2name = input('Player 2, please enter your name: ')
    pp1 = 0 
    pp2 = 0

    while True:
        picked_word = choose()    
        qn = jumble(picked_word)
        print("\nJumbled word:", qn)

        # Player 1 turn
        print(p1name, 'your turn.')
        ans1 = input('What is on my mind? ')
        if ans1 == picked_word:
            pp1 += 1
            print('✅ Correct! Your score is:', pp1)
        else:
            print('❌ Wrong answer! Let’s see if', p2name, 'can guess...')

            # Player 2 turn only if Player 1 is wrong
            print(p2name, 'your turn.')
            ans2 = input('What is on my mind? ')
            if ans2 == picked_word:
                pp2 += 1
                print('✅ Correct! Your score is:', pp2)
            else:
                print('❌ Wrong again! The correct word was:', picked_word)

        # Continue or quit
        c = input('\nPress 1 to continue and 0 to quit: ')
        if c == '0':
            thank(p1name, p2name, pp1, pp2)
            break

play()
