import random


list = []
maximum_bet = 2000
amount_of_guess = random.randint(1, 5)
while amount_of_guess > 0:
    guess = int(input())
    list.append(guess)

    amount_of_guess -= 1
    if guess == maximum_bet:
        print('K')
        exit()


if guess != maximum_bet:
    print(f'{max(list)} diyen ')