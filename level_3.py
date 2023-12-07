import sys


errors = {'type': "Error: The code must be of type string",
          'len': "Error: The code must have 4 characters",
          'char_type': "Error: The code must contain only digits or lower case letters"}
token = 'T1:MDU7S2'

def cipher(code):
    global errors, token

    if type(code) != str:
        sys.exit(errors['type'])
    elif len(code) != 4:
        sys.exit(errors['len'])
    elif not legal_characters(code):
        sys.exit(errors['char_type'])
    elif code == 'r2d2':
        print('Congratulations! you cracked level 3!')
        return token
    else:
        return False

def legal_characters(code):
    for c in code:
        if not (c.isnumeric() or c.islower()):
            return False
    return True