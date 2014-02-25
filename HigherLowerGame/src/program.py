import random

print('**************************************************************');
print('hello, a random number between 1-10 is calculated.');
print('Guess which number has been chosen and enter your choice.');
print('You have 3 tries.');
print('**************************************************************');

playAgain = "y";

while (playAgain == 'y' or playAgain == 'Y'):
    counter = 0;
    randomDigit = random.randrange(1, 10, 1);
    while counter < 3:
        try:
            data = int(input('Enter your choice now: \n'));
        except ValueError:
            print('Not an integer!\n');
            continue;
        if data == randomDigit:
            print('You are right!\n');
            break;
        elif data > randomDigit:
            print('The number is smaller than your input\n');
            counter = counter + 1;
        elif data < randomDigit:
            print('The number is bigger than your input\n');
            counter = counter + 1;
    print('The number was:', randomDigit);  
    playAgain = input('Do you want to play again?\nPress Y/y to continue.\n')

