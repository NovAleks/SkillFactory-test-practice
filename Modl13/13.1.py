def is_leap_year(x):
    return (x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0))
print(is_leap_year(int()))

#money(x)>1000; years(y)>=14.
x = int(input("сумма на карте:"))
y = int(input("Ваш возраст:"))
print(x > 1000 and y >= 14)
