

start_msg = ('---------- Welcome to level 7 ----------\n'
             'Remember that the cipher function may now return values - thous values matter.\n'
             'Also, the cipher function may need more than one input.\n')
keys = [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0,
        0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1,
        1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
locks_opened = [False for i in range(len(keys))]

print(start_msg)

def cipher_cracked(locks, blocked):
    if not blocked and all(locks):
        print('\nCongratulations! you cracked level 7!')
        exit()

def cipher(lock_number, key):
    global locks_opened
    blocked = False

    if type(lock_number) != int:
        exit('Error: the first argument (lock_number) must be an integer')
    elif type(key) != bool:
        exit('Error: the second argument (key) must be a boolean')
    elif lock_number < 0 or lock_number >= len(keys):
        exit('Error: lock_number (first argument) is invalid, there are only locks with numbers 0 - 99')
    else:
        if locks_opened[lock_number]:
            exit(f'Error: lock number {lock_number} was already opened, can\'t enter a key again')
        elif key == keys[lock_number]:
            locks_opened[lock_number] = True
            print(f'Cipher: Lock number {lock_number} was successfully opened')
            cipher_cracked(locks_opened, blocked)
            return True
        else:
            print(f'Cipher: Entered wrong key to open lock number {lock_number}')
            cipher_cracked(locks_opened, blocked)
            return False
