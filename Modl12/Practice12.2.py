print (0.1+0.1*5-0.3*4)

print ((3.14+0.3)/2+0.15)

a = -13
b = 7

a = a-b
b = a+b

print(b)

print(1.57*3/1.5 == 3.14)
print('PY' in "Python")

date = (1, 'january', 2020)
print(date[0])
# 1
print(date[1])
# january
print(date[2])
# 2020

s1 = "foo"
s2 = "bar"
s1 = s1+s2
print(s1)
# foobar
s1 = "foo"
print(id(s1), s1) #проверяем идентификатор
# 139953609727144, foo

s2 = "bar"
print(id(s2), s2) #проверяем идентификатор
# 139953609727088, bar

s1 = s1+s2
print(id(s1), s1) #проверяем идентификатор
# 139953459591296, foobar
