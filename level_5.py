

start_msg = '---------- Welcome to level 5 ----------\n'
the_code = 4673

print(start_msg)

def digit_sum(n):
    n_lst = list(str(n))
    for j, d in enumerate(n_lst):
        n_lst[j] = int(d)
    return sum(n_lst)

def cipher(code):
    global the_code

    if type(code) != int:
        exit('Error: the code must be an integer')
    elif code < 0 or code > 10000:
        exit('Error: the code must be in the range 0 - 10000')
    elif digit_sum(code) == 18:
        exit('Error: I don\'t like numbers who\'s digits sum to 18:(')
    elif code != the_code:
        return False
    else:
        print('Congratulations! you cracked level 5!')
        return True
