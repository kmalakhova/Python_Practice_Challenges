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
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

```python
print('Enter "q" to exit.')

numbers = {}
while True:
  user_number = (input('Enter an integer: '))

  if user_number.lower() == 'q':
    break
  else:
    user_number = int(user_number)

  for i in range(1, user_number+1):
    numbers[user_number] = i*i

print('\nPrinting the results\n...\n')

for key, value in numbers.items():
  print(f'{key}: {value}')
```
