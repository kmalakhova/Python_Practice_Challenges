## 100+ Python challenging programming exercises for Python 3

### Question 1
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method

```python
numbers = []
for number in range(2000, 3201):
  if number % 7 == 0 and number % 5 != 0:
    numbers.append(str(number))

print(','.join(numbers))
```

### Question 2
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Option 1:
```python
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

num = int(input('Enter an inger: '))

print(f'The factorial of number {num} is {factorial(num)}.')
```

Option 2:
```python
def factorial(num):
  fact = 1
  if num == 0:
    return 1
  else:
    for i in range (1, int(num) + 1):
      fact = fact * i
    return fact

num = int(input('Enter an inger: '))

print(f'The factorial of number {num} is {factorial(num)}.')
```

### Question 3
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

```python
print('Enter "q" to exit.')

number_square = {}
while True:
  user_input = (input('Enter an integer: '))

  if user_input.lower() == 'q':
    break    

  if user_input.isdigit():
    user_number = int(user_input)
  else:
    print(f'Entered value "{user_input}" is not an integer.')
    continue

  for i in range(1, user_number+1):
    number_square[user_number] = i*i

if number_square:
  print('\nPrinting the results\n...') 
  for key, value in number_square.items():
    print(f'{key}: {value}')    
else:
  print('\nYou didn\'t enter any number.')
```
