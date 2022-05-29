for i in range(10):
    a = int(input('Type in the first number: '))
    b = int(input('Type in the second number: '))
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print('GCD equals', a)
