"""
File: hailstone.py
Name: Jade Yeh
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

# This constant controls when to stop
EXIT = 1


def main():
    """
    User give a real number and the coder will follow below rule continuously until reach 1.
        Rule: (1) If a given number(n) is odd, coder will multiple x by 3 and then plus 1: n -> 3n + 1
             (2) if a given number(n) is even, coder will divide x by 2: n -> n/2
    """
    print('This program computes Hailstone sequences.')
    print('')
    # num = User's input
    num = int(input('Enter a number: '))
    n = num
    # t = number of steps to reach 1
    t = 0
    # check if User's input equals 1
    if n == EXIT:
        print('It took ' + str(t) + ' steps to reach 1.')
    else:
        # compute continuously while User's input does not equal 1
        while n != EXIT:
            # check whether a number is odd or even before adopting rule (1) or (2)
            if n % 2 == 1:
                # n is odd
                n1 = int(3 * n + 1)
                print(str(n) + ' is odd, so I make 3n+1: ' + str(n1))
                # return calculated value(n1) -> n
                n = n1
            else:
                # n is even
                n1 = int(n / 2)
                print(str(n) + ' is even, so I take half: ' + str(n1))
                # return calculated value(n1) -> n
                n = n1
            #  count steps
            t += 1
        # print result after a given number reach 1
        print('It took ' + str(t) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
