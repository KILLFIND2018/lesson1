#Кортеж и его операции
immutable_var = 1234, 'string', True, 1.5, [1,2,3]
print('Immutable tuple:',immutable_var)

#кортеж не изменяемый по типам значений не сами значения элементов
#immutable_var[0] = 1
#print(immutable_var)

#кортеж не изменяемый по типам значений не сами значения элементов
#immutable_var[1] = "chahge"
#print(immutable_var)

#кортеж не изменяемый по типам значений не сами значения элементов
#immutable_var[2] = False
#print(immutable_var)

#кортеж не изменяемый по типам значений не сами значения элементов
#immutable_var[3] = 1.8
#print(immutable_var)
#в данном случае есть список, он даст нам измений значения внутри элементов  в этом списке
immutable_var[4][0]= 3
print('Changed Only list Immutable tuple:',immutable_var)

#------------------------------------------
#Список и его операции
mutable_list = [0000, 'Строка', False, 2.9, [0,10,6]]
print('Mutable List:' ,mutable_list)
mutable_list[0] = 1111
mutable_list[1] = 'CHANGED'
mutable_list[2] = True
mutable_list[3] = 3.0
mutable_list[4][0] = 10000
print('Changed Mutable List:' ,mutable_list)