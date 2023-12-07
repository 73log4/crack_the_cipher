import sys


errors = {'type': "Error: The code must be of type string",
          'len': "Error: The code must have 2 characters",
          'numeric': "Error: The code must contain only digits"}
token = 'T1:PGEZJGH3'

def cipher(code):
    global errors, token

    if type(code) != str:
        sys.exit(errors['type'])
    elif len(code) != 2:
        sys.exit(errors['len'])
    elif not code.isnumeric():
        sys.exit(errors['numeric'])
    elif code == '32':
        print('Congratulations! you cracked level 1!')
        return token
    else:
        return False