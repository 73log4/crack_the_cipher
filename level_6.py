
start_msg = '---------- Welcome to level 6 ----------\n'
countdown_level = 999

print(start_msg)


def change_countdown_level(b):
    global countdown_level
    if b:
        countdown_level -= 1
    else:
        countdown_level += 1

def cipher(b):
    if type(b) != bool:
        exit('The input can only be boolean value')
    elif countdown_level % 100 == 0:
        change_countdown_level(not b)
    else:
        change_countdown_level(b)
    if countdown_level == 0:
        print('Congratulations! you cracked level 6!')
        return True
    print(f'the count-down level is : {countdown_level}')
    return False
