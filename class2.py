from fsspec.utils import other_paths


class Human:
    def __init__(self, name, age):
        #объект и это как пространство имен
        self.name = name
        self.age = age
    #метод который показывает наши х-ки объектов

    def  __len__(self):
        return self.age

    def __lt__(self, other):
        #если меньше
        return self.age < other.age
    #оператор больше
    def __gt__(self, other):
        return self.age > other.age
    #равно
    def __eq__(self, other):
        return self.age == other.age
    # истина или ложь
    def __bool__(self):
        return bool(self.age)
    #отображение в виде строки
    def __str__(self):
        return f'{self.name}'

den = Human('den', 22)
max = Human('max',23)
print(den < max)
print(den>max)
print(den == max)
print(den)