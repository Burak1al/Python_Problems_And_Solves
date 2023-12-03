import random

#ASCII ÇİZİMLERİNİ FALAN YAPABİLİRİM !!!! TAM BİTMEDİ DAHA

print('Welcome to Hangman. ')
print('You can choose to select your own word or play with the default words. ')
print('Rules - You can guess for a letter in the word or guess the entire word at once. ')
print('6 mistakes and its game over. ')
choice_of_word = input("Enter a word to play with it or press enter to play with the defaults. ")

words = ["python", "programlama", "oyun", "eğlence", "öğrenme"]

if choice_of_word == '':
    words = random.choice(words)
else:
    words = choice_of_word

the_letters = []

for let in words:
    the_letters.append(let)

correctly_guessed_letters = []

game_is_going = True
count_guess = 0
wrong_guess_count = 0
already_guessed = False

while game_is_going:
    guess = input('Give it a guess --> ').lower()
    if guess in correctly_guessed_letters:
        print("You've already guessed that >:( ")
        wrong_guess_count += 1
        already_guessed = True

    if guess in the_letters:
        if guess != '':
            if already_guessed is False:
                print(f'{guess} is a correct guess! ')
                right_amount = the_letters.count(guess)
                for x in range(right_amount):
                    correctly_guessed_letters.append(guess)
        elif guess == '':
            print('type smn bitch')

    elif guess == '':
        print('type smn bitch')

    elif guess == words:
        print('CORRECT')
        exit()

    else:
        wrong_guess_count += 1
        print(f"You've made {wrong_guess_count} wrong guesses. ")
        if wrong_guess_count != 6:
            print(f'{6-wrong_guess_count} guesses left. ')
        elif wrong_guess_count == 6:
            print('You lose. ')
            exit()
        else:
            print('Nope.')

    unique_letters = list(set(the_letters))
    unique_corrects = list(set(correctly_guessed_letters))
    if len(unique_corrects) == len(unique_letters):
        if len(unique_corrects) and len(unique_letters) != 0:
            if wrong_guess_count < 6:
                print('Correct.')
                game_is_going = False
