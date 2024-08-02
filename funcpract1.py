# найти максимум в списке
def find_max(list):
    # берем элемент из списка
    max = list[0]
    for i in list:
        # сравниваем потом завершаем как закончился список
        if i > max:
            max = i
    return max


print(find_max([1, 54, 15, -5, 6]))
#поиск и показать количество четных чисел
def count_even(list):
    counter = 0
    for i in list:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter

print(count_even([2,6,32,5,8,1,0]))

#Уникальный список

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list


print(unique([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]))