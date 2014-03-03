def main():
    print('Enter the message you want to encrypt: ')
    myText = input();
    print('Enter the key you want to encrypt with: ')
    myKey = input();
    encryptedText = encrypt(myText,myKey)
    print (encryptedText)

def encrypt(text, key):
    col = 0
    i = 0
    #### puffertext gets all chars from the pointer (= 1 col)
    puffertext = ''
    #### ciphertext contains all puffertexts (= int(key) * puffertext
    ciphertext = ['']*int(key)
    #######################################
    # you do this 'key times'
    # e.g. key = 4
    # Hi my name is Stefan
    # >i m> na>e i> St>fan
    # H> my>nam> is>Ste>an
    # Hi>my >ame>is >tef>n
    # Hi >y n>me >s S>efa>
    # ====================================
    # The 5th would be the same as the 1st
    #######################################
    while col < int(key): 
        ii = 0
        #### That's the algorithm to get the pointer (= ^ in the above example):
        pointer = col + ii * int(key)
        #### Empty the puffer after each key length
        puffertext = ''
        while pointer < len(text):
            puffertext += text[pointer]
            ii += 1
            pointer = col + ii * int(key)
        ciphertext[col] = puffertext
        col += 1
    return ''.join(ciphertext)
        

if __name__ == '__main__':
    main()
