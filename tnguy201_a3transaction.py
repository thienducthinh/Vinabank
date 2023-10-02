# Thomas Nguyen CIS 345 13088 10:30 AM - 11:45 AM
import csv
import json
import os
import tnguy201_logger
from tnguy201_logger import customers
import time

print('Welcome to Cactus Bank')
print('*********************************')
print('* Enter 1 to add a new customer *')
print('* Enter 2 to delete a customer  *')
print('* Enter 3 to make transactions  *')
print('* Enter 4 to exit               *')
print('*********************************')

tries = 1
max_tries = 3
pin_found = False
logger = []

def format_money(dollar):
    return f'${dollar:.2f}'

while True:
    try:
        selection = int(input('Make your selection: '))
        if selection not in range(1, 5):
            raise Exception
        break
    except (ValueError, TypeError, Exception):
        print('Selection should be 1, 2, 3, or 4.  Try again .....')

if selection == 4:
    exit()

if selection == 1:
    username = input("Please enter your username: ")
    customers[username] = dict()
    tnguy201_logger.create_pin(username)

    customers[username]['Name'] = input('Please enter your name: ')
    try:
        customers[username]['C'] = float(input('Enter the amount you will deposit to the checking account: '))
        if customers[username]['C'] < 0:
            raise TypeError
    except TypeError:
        print('A negative number was entered. The current balance will be 0.0')
        customers[username]['C'] = 0
    except ValueError:
        print('Invalid number entered. The current balance will be 0.0')
        customers[username]['C'] = 0
    try:
        customers[username]['S'] = float(input('Enter the amount you will deposit to the saving account: '))
        if customers[username]['S'] < 0:
            raise TypeError
    except TypeError:
        print('A negative number was entered. The current balance will be 0.0')
        customers[username]['S'] = 0
    except ValueError:
        print('Invalid number entered. The current balance will be 0.0')
        customers[username]['S'] = 0
    print("Your account has been created")
    print("Please visit the system again to make transactions")
    input("Press Enter to continue...")
    # os.system('cls') for windows
    os.system('clear')

elif selection == 2:
    username = input("Please enter a username: ")
    if username in customers:
        customers.pop(username)
        print(f'Customer {username} has been deleted.')
    else:
        print('ERROR: username is not in the system.')

else:
    username = input("Please enter your username: ")
    if username not in customers:
        print('ERROR: username is not in the system.')
    else:
        while tries <= max_tries:
            # Print bank title and menu
            print(f'{"Cactus Bank":^30}\n')
            selection = input('Enter pin or x to exit application: ').casefold()

            if selection == 'x':
                quit()
            elif int(selection) != customers[username]['Pin']:
                # os.system('cls') for windows
                os.system('clear')

                print(f'Invalid pin. Attempt {tries} of {max_tries}. Please Try again')
                if tries == max_tries:
                    ans1 = input('Do you want to get a new pin (y/n)? ')
                    if ans1 == 'y':
                        tnguy201_logger.create_pin(username)
                    else:
                        quit()
                # increment tries
                tries += 1
            else:
                tries = 1
                pin = int(selection)
                print('Correct pin entered! You can make up to 4 transactions!')
                print('To make more than 4 transactions, you will need to re-enter you pin correctly.')
                input()
                # os.system('cls') for windows
                os.system('clear')

                trans = 1
                max_trans = 4
                while trans <= max_trans:

                    print(f"Welcome {customers[username]['Name']}")

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
                            print('Transaction instructions:')
                            print(' - Withdrawal enter a negative dollar amount: -20.00.')
                            print(' - Deposit enter a positive dollar amount: 10.50')

                            print(f'\nBalance:  ${customers[username][selection]: .2f}')
                            old_balance = customers[username][selection]
                            try:
                                amount = float(input(f'Enter transaction amount: ').casefold())
                            except ValueError:
                                print('Bad Amount - No Transaction.')
                                print(f'Transaction complete. New balance is {customers[username][selection]: .2f}')

                            else:
                                if (amount + customers[username][selection]) >= 0:
                                    customers[username][selection] += amount
                                    print(f'Transaction complete. New balance is {customers[username][selection]: .2f}')
                                else:
                                    print('Insufficient Funds. Transaction Cancelled.')
                            finally:
                                logger.append([time.ctime(), username, format_money(old_balance), format_money(amount), format_money(customers[username][selection])])
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
                                trans = max_trans + 1
                                tries = max_tries + 1
                            else:
                                trans += 1
                        break

tnguy201_logger.log_transaction(logger)

with open('customers.json', 'w') as fp:
    json.dump(customers, fp)

# for verification purposes
print('\n\n')
print('Saving data...\n')
print('Data Saved.')
print('Exiting...')

with open('transactions.csv') as log_data:
    data = csv.reader(log_data)
    for row in data:
        print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")