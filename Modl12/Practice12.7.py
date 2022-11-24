#Ввожу сумму инвестирования
money = int(input("Введите сумму которую инвестируете:"))
#Создаю словарь с процентными ставками банков
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#выделяю процентные ставки банков в список
procent = list(per_cent.values())
#записываю доход в каждом банке в переменнуые и округляю
bankTKB = round(procent[0]/100*money)
bankCKB = round(procent[1]/100*money)
bankVTB = round(procent[2]/100*money)
bankSBER = round(procent[3]/100*money)
# создаю список с возможными доходами
deposit = [bankTKB, bankCKB, bankVTB, bankSBER]
# вывожу в консоль список возможных доходов
print("Возможный доход:", deposit)
#сортирую список доходов
deposit.sort()
#вывожу максимальный доход
print("Максимальная сумма, которую вы можете заработать - ", deposit[-1])