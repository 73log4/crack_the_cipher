start_msg = '---------- Welcome to level 9 ----------\n'
instruction = ("Go the wikipedia page of minecraft. Scroll down to the nether section. Click on the first link in "
               "that section."
               " Read the description of the top image on that page. Then enter the number in the description"
               " of the image into the cipher")
print(start_msg)

def cipher(n):
    if type(n) != int:
        exit('Error: the input must be an integer')
    elif n == 1180:
        print('\nCongratulations! you cracked level 9!')
        exit()
    elif n < 0 or n >= len(instruction):
        exit(f'Error: input can only be in the range 0-{len(instruction)}')
    return instruction[n]