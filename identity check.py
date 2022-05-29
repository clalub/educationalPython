print('Hello!')
name = input('What\'s your name? ')
if name != 'Alice':
    print('Go away! Press ENTER to exit.')
else:
    print('Let me ask you one more question.')
    age = input('How old are you? ')
    if age == '30':
        print('Nice to see you again, Alice!')
    elif age < '30':
        print('You\'re not my Alice. You\'re too young. Press ENTER to exit.')
    elif age > '30':
        print('You\'re not my Alice. You\'re too old. Press ENTER to exit.')
