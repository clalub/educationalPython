shape = input('Choose a shape in order to calculate its area: triangle, rectangle, trapezium. ')

if shape == 'triangle':
    def area1(a, h):
        return a * h // 2
    base = int(input('Type in the length of the base: '))
    height = int(input('Type in the height: '))
    area1(base, height)
    print('The area of the triangle equals: ', area1(base, height))

elif shape == 'rectangle':
    def area2(a, b):
        return a * b
    side1 = int(input('Type in the length of the first side: '))
    side2 = int(input('Type in the length of the second side: '))
    area2(side1, side2)
    print('The area of the rectangle equals: ', area2(side1, side2))

elif shape == 'trapezium':
    def area3(a, b, h):
        return (a + b) * h // 2
    trapeziumBase1 = int(input('Type in the length of the first base: '))
    trapeziumBase2 = int(input('Type in the length of the first base: '))
    trapeziumHeight = int(input('Type in the height: '))
    area3(trapeziumBase1, trapeziumBase2, trapeziumHeight)
    print('The area of the trapezium equals: ', area3(trapeziumBase1, trapeziumBase2, trapeziumHeight))

else:
    print('You haven\'t chosen a shape, try again.')

