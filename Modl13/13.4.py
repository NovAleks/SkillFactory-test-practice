# Тема - Условия

#f Условие:
#    Блок инструкций 1
#else:
#    Блок инструкций 2

is_rainy = True  # дождь будет

if is_rainy:
    print("Брать зонт")
else:
    print("Не брать зонт")

s = 5
a = 10
if a > 0:
   s = s + a
else:
   s = s - a

print(s)

is_rainy = True  # дождь будет
heavy_rain = False  # не сильный дождь

if is_rainy:
    # в данный блок дописали ещё один условный оператор
    if heavy_rain:
        print("Брать зонт")
    else:
        print("Надеть дождевик")
else:
    print("Не брать зонт")

