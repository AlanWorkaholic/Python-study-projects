# поиск имени Джон
colleges = ['Max','John','Samuel','Barbara']
names_to_search = ['John']
print(colleges)
print(names_to_search)
for name in colleges:
    if name in names_to_search:
        print('есть совпадение')
        break
else:
    print('совпадений не найдено')
