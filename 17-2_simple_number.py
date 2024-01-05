def is_prime(ccc):
    b = True
    for i in range(2,a-1):
        if a % i == 0:
            #print('число непростое')
            b = False
            break
    if a in (1,2,3):
        b = True
        #print('число простое')
    else:
        if b:
            b = True
            #print('число простое')
    if b:
        return True
    else:
        return False

print('Введите число')
a = int(input(''))
print(is_prime(a))