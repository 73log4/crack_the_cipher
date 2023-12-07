

start_msg = ('---------- Welcome to level 4 ----------\n'
             'From this level on the cipher function has memory, so it remembers what were your inputs\n'
             'It may use some of your last inputs, but maybe also it won\'t')
last_input = None
the_code = 7117

print(start_msg)

def cipher(code):
    global last_input, the_code

    if type(code) != int:
        exit('Error: the code must be an integer')
    elif code < 0 or code > 10000:
        exit('Error: the code must be in the range 0 - 10000')
    elif last_input and last_input + 1 == code:
        exit('Error: can\'t enter consecutive numbers one after the other (for example entering 67 and then 68)')
    elif code != the_code:
        last_input = code
        return False
    else:
        print('Congratulations! you cracked level 4!')
        return True
