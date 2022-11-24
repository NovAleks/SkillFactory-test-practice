numbers = input("Введите числа через пробел:")

numbers_split = numbers.split()
numbers_lines = "\n".join(numbers_split)

print(numbers_lines)

int_num = int(input("Введите целое число: ")) # вводим, например, 256

print(int_num)
# 256
print(type(int_num)) # убеждаемся, что тип данных в переменной - int
# <class 'int'>


age = 25
# my_age = "I'm " + age
# здесь возникнет ошибка
# TypeError: must be str, not int
my_age = "I'm " + str(age)
print(my_age)
# I'm 25


age = 25
my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d
print(my_age)
# I'm 25 years old

# %d, %i Целое число.
# %5d, %12d Выделяет пространство 5 (или любое другое число) символов под это число.
# Выравнивание вправо, остальное пространство остается пустым.
# %05d Также выделяется пространство в 5 символов, но свободное пространство слева заполняется нулями.


pi = 31.4159265
print ("%.4e" % (pi))


day = 14
month = 2
year = 2012
print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2


# HH:MM:SS
hours = 12
minutes = 1
seconds = 59
print("%d:%02d:%d" % (hours, minutes, seconds))
