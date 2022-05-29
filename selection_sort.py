n = 5
a = [0] * n

def input_data():
    for i in range(n):
        a[i] = int(input('Type in a number: '))

def output_data():
    for i in range(n):
        print(a[i])

def max_select(start_i):
    max_i = start_i
    maxx = a[max_i]
    for i in range(start_i + 1, n):
        if a[i] > maxx:
            max_i = i
            maxx = a[max_i]
    return max_i

def sort_select():
    for i in range(n-1):
        max_i = max_select(i)
        t = a[i]
        a[i] = a[max_i]
        a[max_i] = t

input_data()
sort_select()
print('The numbers sorted by selection: ')
output_data()

input('\nPress ENTER to exit.')
    
