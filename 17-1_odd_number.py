def is_odd(number):
    '''
    если число нечетное, то true
    '''
    if number % 2 == 0:
        return False
    else:
        return True
print('Введите число')
a = input()
b = is_odd(int(a))
print(b)