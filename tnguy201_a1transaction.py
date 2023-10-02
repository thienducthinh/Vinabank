# Thomas Nguyen CIS 345 13088 10:30 AM - 11:45 AM
# os allows us to clear the screen in a actual console or terminal
import os
import random

# TODO: modify the users data structure
# key = username, value = account dictionary
# account dictionary has 4 items
# Create objects for balances and transaction
accounts = {'selin2': {'Pin': 9999, 'Name': 'John Doe', 'C': 472.04, 'S': 1000}, 'abcd5': {'Pin': 1234, 'Name': 'Jane Doe', 'C': 1.78, 'S': 2000.01}}
# account = 1000.00
# pin = 0
ans = ''

# Allow 3 invalid pin entries
tries = 1
pin_tries = 1
max_tries = 3
pin_found = False

username = input('Welcome to Cactus Bank.  Please enter your username: ')

if username not in accounts:
    print(f"{username}, Didn't find your username.")
    ans = input("Do you want to create an account (Y/N)? ").lower()
    if ans[0] != 'y':
        print('Thank you for visiting Catcus Bank.  Come back soon.')
        tries = max_tries + 1
    else:
        accounts[username] = dict()
        ans1 = int(input('Enter 1 to create a pin yourself or 2 and the system will create a pin for you: '))
        if ans1 == 1:
            while pin_tries <= max_tries:
                pin = int(input('Select a number between 1 and 9999 as your pin: '))
                print(pin)
                if 0 < pin < 10000:
                    accounts[username]['Pin'] = pin
                    pin_found = True
                    pin_tries = max_tries + 1
                else:
                    print('Invalid pin entered.')
                    pin_tries += 1
                    if pin_tries > max_tries:
                        print('Please try later ....')
                        tries = max_tries + 1
        elif ans1 == 2:
            pin = random.randint(1, 9999)
            print("Your pin is: ", pin)
            accounts[username]['Pin'] = pin
            tries = 1
            pin_found = True
        else:
            print('Invalid option! Thank you for visiting Catcus Bank.  Come back soon.')
            tries = max_tries + 1

    if pin_found:
        accounts[username]['Name'] = input('Please enter your name: ')
        try:
            accounts[username]['C'] = float(input('Enter the amount you will deposit to the checking account: '))
            if accounts[username]['C'] < 0:
                raise TypeError
        except TypeError:
            print('A negative number was entered. The current balance will be 0.0')
            accounts[username]['C'] = 0
        except ValueError:
            print('Invalid number entered. The current balance will be 0.0')
            accounts[username]['C'] = 0
        try:
            accounts[username]['S'] = float(input('Enter the amount you will deposit to the saving account: '))
            if accounts[username]['S'] < 0:
                raise TypeError
        except TypeError:
            print('A negative number was entered. The current balance will be 0.0')
            accounts[username]['S'] = 0
        except ValueError:
            print('Invalid number entered. The current balance will be 0.0')
            accounts[username]['S'] = 0
        print("Please remember your pin.")
        print("The system will require you to enter it again.")
        input("Press Enter to continue...")
        # os.system('cls') for windows
        os.system('clear')

while tries <= max_tries:
    # Print bank title and menu
    print(f'{"Cactus Bank":^30}\n')
    selection = input('Enter pin or x to exit application: ').casefold()

    # determine exit, pin not found, or correct pin found
    if selection == 'x':
        exit()
    # FIXME: Verify entered pin is the same as the pin stored in the accounts dictionary
    elif int(selection) != accounts[username]['Pin']:
        # clear screen - cls for windows and clear for linux or os x
        # os.system('cls')
        os.system('clear')

        print(f'Invalid pin. Attempt {tries} of {max_tries}. Please Try again')
        if tries == max_tries:
            print('Locked out!  Exiting program')
        # increment tries
        tries += 1
    else:
        # Upgrade: successful pin entry. reset tries and save pin
        tries = 1
        pin = int(selection)
        print('Correct pin entered! You can make up to 4 transactions!')
        print('To make more than 4 transactions, you will need to re-enter you pin correctly.')
        input()
        # clear screen
        # os.system('cls')
        os.system('clear')

        trans = 1
        while trans <= 4:

            # TODO: Welcome customer
            # Display Welcome <Customer Name>
            # accounts[username]['Name'] holds a dictionary where 'Name' is the key
            # to the customer's name value
            print(f"Welcome {accounts[username]['Name']}")

            # TODO: Add prompt for Checking or Savings
            # Entry must be C or S to use as a key for the account balances
            # Use a loop and exception handling to ensure input is good
            # reuse selection name to store input to avoid scope issues
            print('   Select Account')
            while True:
                try:
                    selection = input('Enter C or S for (C)hecking or (S)avings: ')
                    if selection != 'C' and selection != 'S':
                        raise ValueError('Incorrect selection. You must enter C or S.')
                except ValueError as ex:
                    print(ex)
                else:
                    os.system('clear')

                    print(f'Opening {selection} Account...\n')
                    # Upgrade: Removed slicing and w/d entry - New Instructions
                    print('Transaction instructions:')
                    print(' - Withdrawal enter a negative dollar amount: -20.00.')
                    print(' - Deposit enter a positive dollar amount: 10.50')

                    # Upgrade: removed for loop only 1 transaction per pin input

                    # FIXME: All references to account need to be fixed
                    # accounts is the new dictionary that needs to be indexed
                    # using the entered username and the selection account type
                    print(f'\nBalance:  ${accounts[username][selection]: .2f}')

                    # TODO: Add exception handling for user entry of amount
                    # Good input - convert to float and store in amount
                    # Exception - Print Bad Amount and set amount to zero
                    try:
                        amount = float(input(f'Enter transaction amount: ').casefold())
                    except ValueError:
                        print('Bad Amount - No Transaction.')
                        print(f'Transaction complete. New balance is {accounts[username][selection]: .2f}')
                    # Upgrade: Verify enough funds in account
                    # FIXME: All references to account need to be fixed
                    # add indices for pin and selection holding account type
                    else:
                        if (amount + accounts[username][selection]) >= 0:
                            accounts[username][selection] += amount
                            print(f'Transaction complete. New balance is {accounts[username][selection]: .2f}')
                        else:
                            print('Insufficient Funds. Transaction Cancelled.')
                    break
            while True:
                try:
                    selection = input('Press n to make another transaction or x to exit application: ')
                    if selection != 'x' and selection != 'n':
                        raise TypeError
                except TypeError:
                    selection = input('Press n to make another transaction or x to exit application: ')
                else:
                    if selection == 'x':
                        exit()
                    else:
                        trans += 1
                break

# end of application loop
