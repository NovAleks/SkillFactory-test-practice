print(31 % 2 + 31 % 2)
print(13 % 3 * 3 - 3**2)

a = 5.4321
print(a)
print(a**100)
# 3.138886636534116e+73

a = 5.4321**100
print(a*100) # мантисса осталась прежней, а степень увеличилась на 2
# 3.138886636534116e+75
print(a*1000) # аналогично, только степень увеличилась уже на 3
# 3.138886636534116e+76
print(a/100) # снова мантисса не меняется, а степень уже уменьшилась
# 3.138886636534116e+71
print(a/1000) # как, наверное, уже ожидаемо, степень снова уменьшилась
# 3.138886636534116e+70

print(round(11*2.5/3, 2))
#Напишите программу, которая вычислит значение выражения 11*2.5/3, округлив до двух знаков после запятой.

print(round(3.14159**2/2))
#Напишите программу, которая вычислит половину квадрата числа Пи (pi=3.14159), округлив до целого.