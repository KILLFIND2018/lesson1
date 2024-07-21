my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index_list = 0

while index_list < len(my_list):
    #В случае если дошли до отрицательных чисел прервать цикл
    if my_list[index_list] < 0:
        break

    if my_list[index_list] > 0:
        print(my_list[index_list])

    index_list += 1