# Caesar Cypher

CONST_LETTERS=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def decrypt(text, key):
    decrypted = ''
    for letter in text:
        num = CONST_LETTERS.find(letter)
        num = num - key;
        # handle wrapping around
        if num < 0:
            num = num + len(CONST_LETTERS)
        decrypted = decrypted + CONST_LETTERS[num]
    return decrypted;

def encrypt(text, key):
    encrypted = ''
    for letter in text:
        num = CONST_LETTERS.find(letter)
        num = num + key;
        # handle wrapping around
        if num >= len(CONST_LETTERS):
            num = num - len(CONST_LETTERS)
        encrypted = encrypted + CONST_LETTERS[num]
    return encrypted;


print('Enter the text you want to decrypt/encrypt:')
text = input()
print('Enter the key as integer value:')
try:
    key = int(input())
except ValueError:
    print ('Input is not an int!')
mode = ''
while mode != 'd' and mode != 'D' and mode != 'e' and mode != 'E':
    print ('For encryption-mode press \'e/E\', for decryption-mode press \'d/D\'')
    mode = input();
if (mode == 'd' or mode == 'D'):
    print('**DecryptionMode**')
    plainText = decrypt (text, key)
    print ('The plain text is: ' + plainText)
else:
    print ('**EncryptionMode**')
    encryptedText = encrypt (text, key)
    print ('The encrypted text is ' + encryptedText)
