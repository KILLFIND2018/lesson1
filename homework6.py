#Словарь
my_dist = {'Tester': 2024, 'Root' : 1885, 'Admin' : 1999}
print("Dist:",my_dist)
#вывод значения одного из ключей
print("Existing value:",my_dist['Root'])
#отсутсвующая пара и вывод без ошибки
my_dist['Testing'] = 2000
print(my_dist['Testing'])
#Добавление пар
my_dist.update({'Alex' : 1995, 'Jonh': 2001})
print("Modified dictionary 1:",my_dist)
#Удаление пары
remover = my_dist.pop('Root')
print("Modified dictionary 2:",my_dist)
print("Deleted value:",remover)

#Множества
my_set =  {222,222,333,3333,333,333,444}
print("Set: ",my_set)
#добавление новых элементов
print(my_set.add((1,9)))
print(my_set.add(6.7))
print("Modified set:",my_set)
#Удаление любого элемента
print(my_set.discard(222))
print("Modified set 2:",my_set)


