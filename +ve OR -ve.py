""" Write a code to check a given number is positive or negative """

x =eval(input("Enter a number to check whether it is Positive OR Negative\n"))
if x > 0:
    print('The Entered Number is POSITIVE as', x, 'is GREATER than ZERO')
elif x == 0:
    print('The Entered Number is neither POSITIVE NOR NEGATIVE as', x, 'is EQUAL ZERO')
else:
    print('The Entered Number is NEGATIVE', x, 'is LESSER than ZERO')
