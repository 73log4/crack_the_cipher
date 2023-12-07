# crack_the_cipher

Crack the Cipher is a fun code-cracking game that teaches python programming and problem solving.

To play the game download the file of the level you want to play. Put it in some folder where you will be playing the game. Create a new python file in that folder where you will write your pyhon solutions. Import to the solutions file the cipher function from the level file:

> from level_{your level} import cipher

Your goal is to 'crack' the cipher function, you do so by calling it with some values. The cipher function will rais an error if there is a problem with your input, and it will return False if you havn't yet cracked the puzzle. If it returns True you solved the level and the cipher function will also print a congratulations message.

The only rules of the game are to not look/change the level file in any way (opening it, importing other functions from it, writig to it, etc...). Other than that do whatever you want to crack the cipher!
