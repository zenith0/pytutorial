'''
Created on 25.02.2014

@author: stefan
'''
import math
def isPythagorean (a, b, c):
    if ((a >= b) and (a >= c)):
        firstSide = b;
        secondSide = c;
        hypothenuse = a;
    elif ((b >= a) and (b >= c)):
        firstSide = a;
        secondSide = c;
        hypothenuse = b;
    elif ((c >= a) and (c >= b)):
        firstSide = a;
        secondSide = b;
        hypothenuse = c;
    if (float(math.pow(firstSide, 2) + math.pow(secondSide, 2))) == float(math.pow (hypothenuse,2)):
        print('Triangle is pythagorean!');
    else:
        print('Triangle is NOT pythagorean!');
    
continueProgram = 'y'


while continueProgram == 'y' or continueProgram == 'Y':
    try:
        firstNumber = float(input('Please enter the lenght of 1 side of the triangle: \n'))
    except ValueError:
        print('Input has to be a digit!');
        continue;
    try:
        secondNumber = float(input('Please enter the lenght of 1 side of the triangle: \n'))
    except ValueError:
        print('Input has to be a digit!');
        continue;
    try:
        thirdNumber = float(input('Please enter the lenght of 1 side of the triangle: \n'))
    except ValueError:
        print('Input has to be a digit!');
        continue;
    #===================================
    # Check if the the triangle is pythagorean 
    #===================================
    isPythagorean(firstNumber, secondNumber, thirdNumber);
    continueProgram = input('Do you want to continue? (y/Y)');
    
    