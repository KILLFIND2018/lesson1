calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    # строку и возвращает кортеж из: длина строки, в верхнем и нижнем регистре
    return (len(string), string.upper(), string.lower())


#проверка совпадений со списоком
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban = urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # не совпало
print(calls)
