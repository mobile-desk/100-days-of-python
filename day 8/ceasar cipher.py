import string

def encrypt(plaintext, shift):
    shifted_alphabet = string.ascii_letters[shift:] + string.ascii_letters[:shift]
    encryption_table = str.maketrans(string.ascii_letters, shifted_alphabet)
    ciphertext = plaintext.translate(encryption_table)
    return ciphertext



plaintext = input("Enter text here: ")
shift = int(input("Enter an integer: "))

ciphertext = encrypt(plaintext, shift)
print(ciphertext)