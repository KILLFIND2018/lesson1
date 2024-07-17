#вывод количества символов в строке
my_string = input("Введите строку: ")
print('Количество символов:', len(my_string))

#Работа с методами
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(" ", ""))
print(my_string[0])
#Хотел реализовать таким образом, но ошибка
lastIndex = len(my_string)
print(my_string[lastIndex])
#
