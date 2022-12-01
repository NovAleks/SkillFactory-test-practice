#дано значение 'n'. Определить входят ли в него цифры 3 и 7.
n = int(input('Введите числа:'))
print('3' in str(n) and '7' in str(n))

###
a = [1, 2, 3]
print(id(a))  # id возвращает идентификатор объекта
# 140039772293512
b = a
print(id(b))
# 140039772293512
print(a is b)  # а и b являются один и тем же объектом
# True

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

# Хорошо
a is None
# Плохо
a == None
