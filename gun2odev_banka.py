balance = 1000
print(f'You currently have {balance}')
transaction = input('Do you wish to withdraw or deposit?  ').lower()
if transaction == 'withdraw':
    ask_amount = int(input('How much do you want to withdraw?  '))
    if ask_amount > balance:
        print('Your balance is insufficient. ')
    else:
        print(f'Transaction successful. Your new balance is {balance-ask_amount}. ')
        print('Have a nice day. ')
elif transaction == 'deposit':
    ask_amount = int(input('How much do you want to deposit?  '))
    print(f'You now have {balance+ask_amount}. ')
    print('Have a nice day. ')
