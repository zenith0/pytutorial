'''
Created on 24.02.2014

@author: stefan
'''


def calculateChange (priceInEuro, amountInEuro):
        
    fiveHundredEuros = 0;
    twoHundredEuros = 0
    oneHundredEuros = 0
    fiftyEuros = 0
    twentyEuros = 0
    tenEuros = 0
    fiveEuros = 0
    twoEuros = 0
    oneEuros = 0

    fiftyCents = 0
    twentyCents = 0
    tenCents = 0
    fiveCents = 0
    twoCents = 0
    oneCents = 0

    result = amountInEuro - priceInEuro
    while result >= 50000:
        fiveHundredEuros = fiveHundredEuros + 1
        result = result - 50000
    while result >= 20000:
        twoHundredEuros = twoHundredEuros + 1
        result = result - 20000
    while result >= 10000:
        oneHundredEuros = oneHundredEuros + 1
        result = result - 10000
    while result >= 5000:
        fiftyEuros = fiftyEuros + 1
        result = result - 5000
    while result >= 2000:
        twentyEuros = twentyEuros + 1
        result = result - 2000
    while result >= 1000:
        tenEuros = tenEuros +1
        result = result - 1000
    while result >= 500:
        fiveEuros = fiveEuros + 1
        result = result - 500
    while result >= 200:
        twoEuros = twoEuros +1
        result = result - 200
    while result >= 100:
        oneEuros = oneEuros + 1
        result = result - 100
    
#### Calculate given prices in Cents
    while result >= 50:
        fiftyCents = fiftyCents + 1
        result = result - 50
    while result >= 20:
        twentyCents = twentyCents + 1
        result = result - 20
    while result >= 10:
        tenCents = tenCents +1
        result = result - 10
    while result >= 5:
        fiveCents = fiveCents + 1
        result = result - 5
    while result >= 2:
        twoCents = twoCents +1
        result = result- 2
    while result >= 1:
        oneCents = oneCents + 1
        result = result - 1
    
    print ('You have to return: \n')
    print (fiveHundredEuros, '500 €')
    print (twoHundredEuros, '200 €')
    print (oneHundredEuros, '100 €')
    print (fiftyEuros, '50 €')
    print (twentyEuros, '20 €')
    print (tenEuros, '10 €')
    print (fiveEuros, '5 €')
    print (twoEuros, '2 €')
    print (oneEuros, '1 €')
    print ('\n')
    print (fiftyCents, '50 c')
    print (twentyCents, '20 c')
    print (tenCents, '10 c')
    print (fiveCents, '5 c')
    print (twoCents, '2 c')
    print (oneCents, '1 c')

check = 'y'

while check == 'y':
    price = float (input ('Enter the price of the item: \n'))
    amount = float (input ('Enter the amount given to you: \n'))

    #### Calculate given prices in Euros
    totalPrice = price*100
    totalAmoount = amount*100
    calculateChange(totalPrice, totalAmoount)
    check = input('Do you want to continue? (y/Y)')




