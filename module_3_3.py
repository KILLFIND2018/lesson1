# Функция  с параметрами по умолчанию
def print_params( a= 1, b = "строка", c = True):
    print(a,b,c)
print_params(6,'test')
print_params(9,'str',False)
print_params(5)
print_params()
#Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25)
print_params(c = [1,2,3])

#Распаковка параметров:
values_list = [123, 'String', False]
values_dict = {'a': 1, 'b' : "строка", 'c' : True}
#Передайте values_list и values_dict в функцию print_params
print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры:
values_list_2 = ['строчка', 39]
#Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)