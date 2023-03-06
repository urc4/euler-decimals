from math import factorial

# there is a limit to float


def user_choice():
    choice = 'wrong'
    while choice == 'wrong':
        choice = input(f'\nHow many decimals places for e?(1-14) ')
        if choice.isdigit() == False:
            choice = 'wrong'
            print(f'\nEnter a valid integer from 1 to 14.')
        elif int(choice) > 14 or int(choice) < 1:
            choice = 'wrong'
            print(f'\nChoose a number from 1 to 14.')

    return int(choice)


def get_number_of_terms(decimal_places):
    term = 0
   #  error used in the polynomial approximation
    while factorial(term+1) <= 3*10**decimal_places:
        term = term + 1
    return term + 1


def calculate_term(term):
    if term == 0:
        return 1
    return 1/factorial(term)


def calculate_e_to_nth_digit(decimal_places):
    number_of_terms = get_number_of_terms(decimal_places)
    e = 0
    for term in range(0, number_of_terms):
        e = e + calculate_term(term)
    result = float(f'{e:.{decimal_places}f}')
    return result


decimal_places = user_choice()
e = calculate_e_to_nth_digit(decimal_places)
print(f'\n\n{e}\n')
