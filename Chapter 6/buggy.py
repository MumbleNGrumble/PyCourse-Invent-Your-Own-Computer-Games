import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

print('What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()

# answer is a string while number1 + number2 results in an integer.
if answer == number1 + number2:
    print('Correct')
else:
    print('Nope! The answer is ' + str(number1 + number2))
