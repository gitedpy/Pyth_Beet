def two_numbers():
    a = input('Please input first number a: ')
    b = input('Please input second number b: ')
    try:
        print(int(a)**2/int(b))
    except ValueError:
        print('You input not number.')
    except ZeroDivisionError:
        print('You cannot divide by zero.')

two_numbers()