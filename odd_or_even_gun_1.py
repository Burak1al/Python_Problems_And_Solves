try:
    n = int(input())
    if not 1<=n<=100:
        print('Please enter a number in the range of 1<= n <= 100')
    elif n % 2 != 0:
        print('Weird')
    elif n in range(2, 5):
        print('Not Weird')
    elif n in range(6, 21):
        print('Weird')
    elif 100 >= n > 20:
        print('Not Weird')
except:
    print('Please enter a number.')