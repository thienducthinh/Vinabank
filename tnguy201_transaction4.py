# Thomas Nguyen CIS 345 13088 10:30 AM - 11:45 AM and PE4
# This is the PE4 starting file.
# Rename the file to [ASUrite]_transaction4.py
# os allows us to clear the screen in a actual console or terminal
import os
# TODO: Add imports for json
import json

# TODO:  Read customers data file into accounts
# use the open command to open the file
# read the file and load the data structure in using json.loads()
# close the file when done
# Read File without using 'with' keyword
# Delete the below line and assign accounts data from file
customers = open('customers.json')
accounts = json.load(customers)
customers.close()

print(accounts)
# Allow 3 invalid pin entries
tries = 1
max_tries = 3

# In this PE exercise, we will only test the existing username
username = input('Welcome to Cactus Bank! Please enter your username: ')

while tries <= max_tries:
    # Print bank title and menu
    print(f'{"Cactus Bank":^30}\n')
    selection = input('Enter pin or x to exit application: ').casefold()

    # determine exit, pin not found, or correct pin found
    if selection == 'x':
        break
    # Verify entered pin is a key in accounts
    elif int(selection) != accounts[username]['Pin']:
        # clear screen - cls for windows and clear for linux or os x
        os.system('cls')
        # os.system('clear') for mac users

        print(f'Invalid pin. Attempt {tries} of {max_tries}. Please Try again')
        if tries == max_tries:
            print('Locked out!  Exiting program')

        tries += 1
    else:
        # Successful pin entry. reset tries and save pin
        tries = 1
        pin = selection

        # os.system('cls')
        os.system('clear')

        for t in range(1, 5):
            # Welcome customer
            print(f"Welcome {accounts[username]['Name']}")
            print(f'{"Select Account": ^20}')

            # Prompt for Checking or Savings
            while True:
                try:
                    selection = input('Enter C or S for (C)hecking or (S)avings: ').upper()
                    if selection != 'C' and selection != 'S':
                        raise ValueError('Incorrect selection.  You must enter C or S.')
                except ValueError as ex:
                    print(ex)
                else:
                    os.system('clear')
                    print(f'Opening {selection} Account...\n')
                    break
            # End Prompt Checking or Savings

            print('Transaction instructions:')
            print(' - Withdrawal enter a negative dollar amount: -20.00.')
            print(' - Deposit enter a positive dollar amount: 10.50')

            # FIXME: Modify the code below to display the selected account's balance with commas for thousands and dot for cents
            print(f'\nBalance:  ${accounts[username][selection]:>,.2f}')

            amount = 0.00
            try:
                amount = float(input(f'Enter transaction amount: '))
            # FIXME: Catch appropriate exceptions not just Exception
            # print better error message details using exception object
            except ValueError as ex:
                print(f'Bad Amount - No Transaction. {ex}')
                amount = 0.00
            except TypeError as ex:
                print(f'Bad Input - No Transaction. {ex}')
                amount = 0.00
            # Verify enough funds in account
            if (amount + accounts[username][selection]) >= 0:
                # FIXME: round() new account balance to 2 decimal places
                # Do this step last after running your program.
                accounts[username][selection] = round((accounts[username][selection] + amount), 2)
                # FIXME: Modify formatting to add commas for thousands
                print(f'Transaction complete. New balance is {accounts[username][selection]:>,.2f}')
            else:
                print('Insufficient Funds. Transaction Cancelled.')

            ans = input('Press n to make another transaction or x to exit application: ').casefold()
            if ans[0] == 'x':
                tries = max_tries + 1
                break

# end of application loop

print('\n\nSaving data...')
# TODO: Write accounts data structure to file
# We can write accounts to our data file here because
# this is after we exit our application loop when
# the user typed x to exit.
with open('customers.json', 'w') as fp:
    json.dump(accounts, fp)
print('\nData Saved.\nExiting...')
