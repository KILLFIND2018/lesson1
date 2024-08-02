def calculate_structure_sum(data_structure):
    summa = 0
    #считаем что есть в словарях по ключам и значениям
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    # считаем что есть в списках, множествах или кортежах
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
    # считаем числа
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
    # длину строк всего и ключей и значений
    elif isinstance(data_structure, str):
        summa += len(data_structure)
    return summa


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)