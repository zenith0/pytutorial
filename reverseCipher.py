# Reverse Cipher

def reverseCipher (text):
    translated = ''
    i = len(string) - 1
    while i >= 0:
        translated = translated + string[i]
        i = i -1
    print (translated)


print ('Enter a string you want to get a reverse cipher')
string = input()
reverseCipher (string)
