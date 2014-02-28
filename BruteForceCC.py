# BruteForce Caesar Cypher

CONST_LETTERS=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def bruteForce(text):
    i = 0
    while i < len(CONST_LETTERS):
        newText = ''
        for letter in text:
            num = CONST_LETTERS.find(letter)
            num = num - i
            if num < 0:
                num = num + len(CONST_LETTERS)
            newText = newText + CONST_LETTERS[num]
        print ('Key is ' + str(i) + '** with decrypted text: ' + newText)
        i = i +1

print ('Enter the text you want to bruteForce:')
text = input()
bruteForce(text)
