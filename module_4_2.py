def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() # вызов внутри фукнции тест

#inner_function() # вне пространства (ошибка)

test_function() #выводит что нам нужно