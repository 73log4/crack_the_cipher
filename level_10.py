import random


start_msg = '---------- Welcome to level 10 ----------\n'
code = [random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9']) for i in range(1000)]
num_code = int(''.join(code))
max_len = 3000
print(start_msg)

def hide_code(c):
    cnt = 0
    hash_code = ""
    while cnt < len(c):
        if random.choice([0, 1]):
            hash_code += str(c[cnt])
            cnt += 1
        else:
            hash_code += random.choice(['?', ',', '_'])
    return hash_code

hidden_code = hide_code(code)
hidden_code += '?' * (max_len - len(hidden_code))

def cipher(n):
    if type(n) != int:
        exit('Error: the input must be an integer')
    elif n == num_code:
        print('\nCongratulations! you cracked level 10!')
        exit()
    elif n < 0 or n >= len(hidden_code):
        exit(f'Error: input can only be in the range 0-{len(hidden_code)}')
    return hidden_code[n]