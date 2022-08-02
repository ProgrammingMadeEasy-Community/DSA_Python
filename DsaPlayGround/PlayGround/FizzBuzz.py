def fizzbuzz():
    count = 3
    while True:

        user_input = int(input('Enter a positive integer: '))
        if count == 0:
            break
        if user_input <= 0:
            count -= 1
            print(
                f'you have {count} trials left, you can only enter a positivenumber,try again!\n')
        else:
            if user_input % 3 == 0 and user_input % 5 == 0:
                print('FizzBuzz')
            elif user_input % 5 == 0:
                print('Buzz')
            elif user_input % 3 == 0:
                print('Fizz')
            else:
                print(str(user_input))


fizzbuzz()
