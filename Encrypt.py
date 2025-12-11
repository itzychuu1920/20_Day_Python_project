import string
import random
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#ENCRYPT PART
def encrypt(plain):
    cipher_text = ""
    for letter in plain:
        index = chars.index(letter)
        cipher_text += key[index]
    print(f"Original message: {plain}")
    print(f"Cipher message: {cipher_text}")
choice = input("Do you want to encrypt a message? (Y/N): ").lower()
if choice == "y":
    plain_text = input("Enter a message to encrypt: ")
    encrypt(plain_text)

#DECRYPT PART
def decrypt(coded):
    plain_text = ""
    for letter in coded:
        index = key.index(letter)
        plain_text += chars[index]
    print(f"Encrypted message: {coded}")
    print(f"Decrypted message: {plain_text}")

choice = input("Do you have a message to decrypt? (Y/N): ").lower()
if choice == "y":
    cipher_text = input("Enter a message to decrypt: ")
    decrypt(cipher_text)
else:
    pass

