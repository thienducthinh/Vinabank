# Thomas Nguyen CIS 345 13088 10:30 AM - 11:45 AM

import os
import random

# Create objects for balances and transactions
users = {'thomas': 2175}
account = 1000.00

# Allow invalid pin tries
tries = 1
pin_tries = 1
max_tries = 3
pin_created = False


user = input('Welcome to Cactus Bank. Please enter your username: ')

if user.casefold() not in users:
    print(f"{user}, Didn't find your user name.")
    choice = input('Do you want to create an account (Y/N)? ').casefold()
    if choice != 'y':
        print("We're sorry that you've decided to leave us.")
    else:
        
        while True:
            try:
                ans = input('Enter 1 to create a pin yourself or 2 and the system will create a pin for you: ')
                if ans < 1 or ans > 2:
                    raise ValueError('Select 1 or 2')
            except TypeError:
                print('Oops!')
            else:
                print('Correct')
                break
        while pin_tries <= max_tries:
            if ans == '1':
                pin = int(input('Select a number between 1 and 9999 as your pin: '))
                print(f'{pin}')
                if pin < 1 or pin > 9999:
                    print('Invalid pin entered.')
                    if pin_tries == max_tries:
                        print('Please try later ....')
                        break
                    pin_tries += 1
                    continue
                else:
                    users[user.casefold()] = pin

            elif ans == '2':
                pin = random.randint(1, 9999)
                print(f'Your pin is: {pin}')
                users[user.casefold()] = pin

            else:
                print('Please try later ....')
                break
            print('Please remember your pin.')
            print('The system will require you to enter it again.')
            print('Press Enter to continue...')
            input()
            os.system('clear')
            while tries <= max_tries:
                selection = input('Enter pin or x to exit application: ').casefold()
                if selection == 'x':
                    break
                elif int(selection) != users.get(user):
                    os.system('clear')
                    print(f'Invalid pin. Attempt {tries} of {max_tries}. Please Try again')
                    if tries == max_tries:
                        print('Locked out! Exiting program')

                    # increment tries
                    tries += 1
                else:
                    os.system('clear')
                    print('Transaction instructions:')
                    print('Enter w for Withdrawal or d Deposit followed by dollar amount.')
                    print('Example withdrawal of $10.50 you would enter w10.50')
                    print('All dollar amounts must be positive numbers')

                    for num in range(1, 5):
                        print(f'\nBalance:  ${account: .2f}')
                        selection = input(f'Enter x to exit application or Enter transaction {num}: ')

                        if selection == 'x':
                            break
                        elif len(selection) >= 2:
                            transaction = selection[:1]
                            amount = float(selection[1:])

                            print(f'Starting balance is {account: .2f}')
                            if transaction == 'w' and amount >= 0:
                                account -= amount
                                print(f'After Withdrawal new balance is {account: .2f}')
                            elif transaction == 'd' and amount >= 0:
                                account += amount
                                print(f'After Deposit new balance is {account: .2f}')
                            else:
                                print('Invalid entry. Please try again.')
                        else:
                            print('Invalid entry. Please try again.')
                    break
            # End transaction loop and also application loop
