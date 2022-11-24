# допустим, у нас есть список, содержащий первые 4 буквы латинского алфавита
letters = ['a', 'b', 'c', 'd']

# с помощью метода append() мы добавляем ещё один элемент в список
letters.append('e')

print(letters)
# ['a', 'b', 'c', 'd', 'e']

print(len(letters))
# 5

# получить доступ к последнему элементу
print(letters[len(letters)-1])
# e

letters.append('f') # добавляем ещё одну букву
letters.append('g') # и ещё одну

print(letters[len(letters)-1])
# g

print(letters[-1])
# g
print(letters[-4])
# d

print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters.pop() # вызов метода без аргументов удаляет последний элемент списка

print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f']
# был удалён последний элемент

letters.pop(0) # или можно удалить элемент по его индексу

print(letters)
# ['b', 'c', 'd', 'e', 'f']
# был удалён нулевой элемент

letters.pop(3) # и не обязательно удалять из начала или конца списка

print(letters)
# ['b', 'c', 'd', 'f']
# был удалён элемент с индексом 3

L = ["а", "б", "в", 1, 2, 3, 4]
print (L[-4::-1]) #[3::-1]
# [1, "в", "б", "а"]

L = ["а", "б", "в", 1, 2, 3, 4]
print (L[-1:3:-1]) #-1:-4:-1 #:3:-1
# [4, 3, 2]

#######

# имеем список с числами с плавающей точкой
L = [3.3, 4.4, 5.5, 6.6]

# печатаем сам объект map
print(map(round, L)) # к каждому элементу применяем функцию округления
# <map object at 0x7fd7e86eb6a0>

# и результат его преобразования в список
print(list(map(round, L)))
# [3, 4, 6, 7]

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел

print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка

########## map

# все операции - деление строки по пробелам, преобразование к числам
# и приведение объекта map к типу список, можно делать в одной строке
L = list(map(float, input().split()))

# обмениваем первое и последнее число
# с помощью множественного присваивания
L[0], L[-1] = L[-1], L[0]

# находим сумму и добавляем её в конец списка
L.append(sum(L))
print(L)

########### словари dict

person = {} # с помощью фигурных скобок можно создать словарь

# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}

# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}

print(person.keys())
# dict_keys(['name', 'age', 'email', 'phone'])

print(person.values())
# dict_values(['Ivan Petrov', 25, 'ivan_petrov@example.com', '8(800)555-35-35'])

d = {'day' : 22, 'month' : 6, 'year' : 2015}
print("||".join(d.keys()))

#########Напишите программу, которая получает на вход название книги - title, фамилию автора - author и год выпуска - year.
#Полученные данные должны быть преобразованы в словарь book с ключами: title, author, year. Причем year нужно преобраовать в тип int.

title = input("Введите название книги:")
author = input("Введите фамилию автора:")
year = int(input("Введите год издания:"))

book = {'title': title,
        'author': author,
        'year': year}

print(book)

####### set{}

text = input("Введите текст:")

unique = list(set(text))

print("Количество уникальных символов: ", len(unique))

########

abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов"}

non_debtors = abons.difference(debtors)

print(non_debtors)
# {'Васильев', 'Иванов'}
