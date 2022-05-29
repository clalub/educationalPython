for i in range(10):
    a = int(input('Type in the first number: '))
    b = int(input('Type in the second number: '))
    while b != 0:
        divisor = b
        b = a % b
        a = divisor
    print('GCD equals', a)

