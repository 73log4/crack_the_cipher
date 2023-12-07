import sys


errors = {'type': "Error: The code must be of type string",
          'len': "Error: The code must have 5 characters",
          'numeric': "Error: The code must contain only digits",
          'division': 'I dont like numbers that are divisible by 11 :('}
token = 'T1:8JC47GFQ'

def cipher(code):
    global errors, token

    if type(code) != str:
        sys.exit(errors['type'])
    elif len(code) != 5:
        sys.exit(errors['len'])
    elif not code.isnumeric():
        sys.exit(errors['numeric'])
    elif int(code) % 11 == 0:
        sys.exit(errors['division'])
    elif code == '99998':
        print('Congratulations! you cracked level 2!')
        return token
    else:
        return False