# This program will be yours personal calculator to change physics units values for SI

# Warning work in progress!

import change_units_functions as cuf

start_program = False
show_help = False
in_program = True

while in_program:
    print ('This program will help you change SI units.\nInput one of the following: \n\t- [s] => start program, \n\t- [h] = > get help, \n\t- [q] => quit\n\nChoice: ', end='')
    try:
        choice_start = input()
    except ValueError:
        print('This is invalid input you should\'ve use STRING. Quitting...')
        quit()

    if choice_start == 's' or choice_start == 'S':
        start_program = True
    elif choice_start == 'h' or choice_start == 'H':
        show_help = True
    elif choice_start == 'q' or choice_start == 'Q':
        quit()

    if start_program:
        print ('\nPlease input value (float): ', end='')
        value = float(input())

        print ('\nPlease input prefix (string): ', end='')
        prefix = input()

        print ('\nPlease input unit (string): ', end='')
        unit = input()

        print ('To what prefix you want to change (string): ', end='')
        to_prefix = input()

        print(str(value) + ' [' + prefix + unit + '] = ' + str(cuf.change_prefix(value, cuf.change_prefix_to_number(prefix), cuf.change_prefix_to_number(to_prefix))) + ' [' + to_prefix + unit + ']')


    if show_help:
        cuf.get_help()
        

    print('Do you want to quit? [y]: ', end='')
    try:
        choice_quit = input()
    except ValueError:
        quit()
    if choice_quit == 'y':
        in_program = False








