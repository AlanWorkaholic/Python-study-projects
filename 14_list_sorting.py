#1 сортировка списка
# colleges = ['Max','Dan','John']
# print('до\n',colleges)
# colleges.sort()
# print('после сортировки\n',colleges)
# print(colleges[1])

#2
#person1 = ('Alan','Subin',36)  # кортеж
#people = list()                # список
#person2 = ('Tex','Gee',30)
#person3 = ('Beek','Ned',25)
#people.append(person1)         # добавление человека в список
#people.append(person2)
#people.append(person3)
#people.sort()                  # сортировка
#print(people)
#del people[2]
#print(people)

#3 проверка наличия имени друга в списке всех имен
friends = {'Илья','Витя','Иван','Саша'}
print(friends)
common_names = {'Иван','Маша','Паша','Саша','Даша'}
common = friends & common_names
print(common)