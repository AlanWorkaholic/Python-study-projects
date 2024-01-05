# проверка, что первая буква имени во второй половине алфавита
name = 'eter'
abc = 'nopqrstuvwxyz'

#if name.lower()[0] in abc:
#    second_half = True
#else:
#    second_half = False

second_half = name.lower()[0] in abc
print(name[0], second_half)