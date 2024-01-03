from level_template import CipherTemplate


class Cipher(CipherTemplate):

    encrypted_mes = ""
    d = {}
    symbols = "0123456789!@#$%^&*()_+=?[]"
    letters = "qwertyuiopasdfghjklzxcvbnm"
    mes = "just enter this text into the cipher function"

    def __init__(self):
        CipherTemplate.__init__(self, 13)

        Cipher.d = {Cipher.letters[i]: Cipher.symbols[i] for i in range(26)}
        Cipher.d[" "] = " "

        Cipher.encrypted_mes = "".join([Cipher.d[c] for c in Cipher.mes])

        self.print_message(Cipher.encrypted_mes)

    def cipher(self, l):
        if l == Cipher.mes:
            self.cracked()
        elif type(l) == str and l in Cipher.letters:
            return Cipher.d[l]
        else:
            self.error("input must be a single letter")


cipher = Cipher().cipher
