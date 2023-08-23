""""
Write a Python program that prints a triangular pattern like the ones shown below in the examples.

Each row must have its corresponding number of asterisks. The first row contains one asterisk. The second row contains two asterisks. The third row contains three asterisks and so on.

The number of rows should be determined by the value of n, a value entered by the user.

If the value of n is 3:

*
* *
* * *
If the value of n is 5:

*
* *
* * *
* * * *
* * * * *

------------------------------------------------
"""

number= int(input("Enter a number"))

num2 = number

while num2 >0:
    for i in range (num2):
        print("*", end = ' ')

    print('')

    num2 -= 1