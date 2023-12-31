import random


start_msg = '---------- Welcome to level 12 ----------\n'
code = "".join([random.choice(['v', 'r', 'a', 'j']) for i in range(1000)])
dict_c = {'v': '?', 'r': '+', 'a': '^', 'j': '*'}
encrypted_code = ''.join([dict_c[a] for a in code])

print(start_msg)


def cipher(n):
    if type(n) != str:
        exit("error: the input must be a string")
    elif n == code:
        print('\nCongratulations! you cracked level 12!')
        exit()
    else:
        print("\n? -> v\n+ -> r\n^ -> a\n* -> some letter (lol I\'m not gonna tell you)\n")
        return encrypted_code