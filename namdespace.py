a = 5
b = 10


def printer():
    # локальное пространство имен, используются только в теле функции
    global a, b  # для вызова внешних переменных и переопределить в этой функции
    a = 'str'
    b = 'str 2'
    c = 20
    d = 30
    print(c, d, 'local')
    print(a, b, 'global')


print(a, b)
printer()
print(a, b)
