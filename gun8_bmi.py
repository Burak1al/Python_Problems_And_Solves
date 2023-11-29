height = float(input('height '))
#boyu 175 değil 1.75 diye yaz
weight = float(input('weight '))
if weight/(height**2) < 18.5:
    print('underweight')
elif 18.5 <= weight/(height**2) < 25:
    print('normal')
elif 25 <= weight/(height**2) < 30:
    print('overweight')
elif weight/(height**2) >= 30:
    print('fatass')