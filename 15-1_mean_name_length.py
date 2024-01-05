# вычисление средний длины имени
colleges = ['Max','John','Samuel','Barbara']
quantity = len(colleges)
length = 0
print('длина имен:')
for name in colleges:
    length += len(name)
    print(len(name),name)
mean = length/quantity
print('количество человек:',quantity)
print('всего букв:',length)
print('средняя длина имени:',mean)