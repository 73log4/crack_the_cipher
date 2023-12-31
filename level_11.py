import random


start_msg = '---------- Welcome to level 11 ----------\n'
code = "".join([random.choice(['1', '2', '3', '4']) for i in range(1000)])
dict_c = {'1': '?', '2': '-', '3': '#', '4': '*'}
encrypted_code = ''.join([dict_c[a] for a in code])

print(start_msg)


def cipher(n):
    if type(n) != str:
        print("error: the input must be a string\n")
    elif n == code:
        print('\nCongratulations! you cracked level 11!')
        exit()
    else:
        print("\n? -> 1\n- -> 2\n# -> 3\n* -> 4\n")
        return encrypted_code