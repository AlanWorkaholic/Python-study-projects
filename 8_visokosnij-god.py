print('Введите год')
year = input('')
print('А теперь проверим является ли он високосным')
print('...')
if int(year) % 4 == 0:
    if int(year) % 100 == 0:
        if int(year) % 400 == 0:
           print('Год високосный')
        else:
            print("Год невисокосный")
    else:
         print("Год високосный")
else:
    print("Год невисокосный")

