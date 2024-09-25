'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''

numbers = {"odd":[], "even":[]}

while True:
    number = int(input("Enter a number (to see list, enter 0):"))
    if number == 0:
        break
    elif number % 2 == 0:
        numbers["even"].append(number)
    else:
        numbers["odd"].append(number)

print(numbers)