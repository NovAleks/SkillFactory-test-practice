A = int(input('Введите целое число:'))
if A % 2 == 0:
    print('Число А кратно 2')
if A % 3 == 0:
    print('Число А кратно 3')
#if A % 2 == 0 or A % 3 == 0:
#    print('Число А кратно 2 или 3')

#######
# Примеры
#if pozitive_num:  # нет смысла проверять len(pozitive_num)
   # если список не пустой, то печатаем его
   #print("Список положительных чисел равен: ", pozitive_num)
#else:
   # печатаем, если список оказался пустым
   #print("Список положительных чисел пустой")

#if not password:  # password строка содержащая пароль, введенный пользователем
   #print("Вы забыли ввести пароль! Повторите попытку ещё раз")

def are_both_odd(A, B):
  if A % 2 == 1 and B % 2 == 1:
    print('Числа А и B нечетные')

######
hour = int(input('введите время в часах:'))
if hour >= 6 and hour < 12:
    print("Утро!!!")
#if 6 <= hour < 12:
#    print("Утро!!!")

########
x = int(input('Введите число координат X:'))
y = int(input('Введите число координат Y:'))
if x > 0 and y > 0:
    print("Первая четверть")
if x > 0 and y < 0:
    print("Четвертая четверть")
if x < 0 and y > 0:
    print("Вторая четверть")
if x < 0 and y < 0:
    print("Третья четверть")

#########if-elif-else
#if a == 10:
#    print('a равно 10')
#elif a < 10:
#    print('a меньше 10')
#else:
#    print('a больше 10')

########
month = int(input('ВВедите число месяца:'))

if month in [3, 4, 5]:
    print("Весна")
elif month in [6, 7, 8]:
    print("Лето")
elif month in [9, 10, 11]:
    print("Осень")
elif month in [12, 1, 2]:
    print("Зима")

