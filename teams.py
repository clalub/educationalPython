for i in range(5):
    print('Type in the number of students', i + 1, end = '')
    a = int(input(': '))
    team = a % 6
    if team == 0:
        print('The number of teams:', a // 6)
    else:
        print('It\'s not possible to allocate all the students to teams.')
