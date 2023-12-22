import random


start_msg = '---------- Welcome to level 11 ----------\n'
code = [random.choice(['1', '2', '3', '4']) for i in range(1000)]
dict_c = {'1': '?', '2': '-', '3': '#', '4': '*'}
encrypted_code = ''.join([dict_c[a] for a in code])

print(start_msg)


def cipher(n):
    if n == code:
        print('\nCongratulations! you cracked level 11!')
    else:
        return encrypted_code + "\n? -> 1\n- -> 2\n# -> 3\n* -> 4\n"