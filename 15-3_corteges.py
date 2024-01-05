# создали список кортежей, убрали кортежи, где не проставлен возраст, посчитали средний возраст
# написал кто старый, кто молодой
people = list()                # список
person1 = ('Matt','Subin',36)  # кортеж
person2 = ('Tex','Gee',30)
person3 = ('Thel','Ban',None)
person4 = ('Like','Me',None)
person5 = ('Beek','Ned',27)
people.append(person1)         # добавление человека в список
people.append(person2)
people.append(person3)
people.append(person4)
people.append(person5)
people_with_age = list()       # создали новый список для людей с проставленным возрастом
for x in people:
    if x[2] is not None:
        people_with_age.append(x)
print([x[2] for x in people])
print([x[2] for x in people_with_age])
quantity = len(people_with_age)
length = 0
for x in people_with_age:
    length += int(x[2])
mean = length/quantity
print('средний возраст',mean,'\n')
for x in people:
    if x[2] is None:
        print(x[0],'возраст неизвестен')
    elif x[2] > mean:
        print(x[0],'старый')
    else:
        print(x[0],'молодой')