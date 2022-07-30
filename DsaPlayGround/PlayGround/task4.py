# Question
# Array and String Manipulation

# Program to print Odd and Even Numbers from an integer Array.
# Input:
#[1, 2, 5, 6, 3, 2]


input = [1, 2, 5, 6, 3, 2]


def even():
    for x in input:
        if x % 2 == 0:
            print(x, 'is an even number')
        else:
            print(x, 'is an odd number')


even()
