class Human:
    def __init__(self, name, age):
        #объект и это как пространство имен
        self.name = name
        self.age = age
    #метод который показывает наши х-ки объектов

    def  __len__(self):
        return self.age


den = Human('den', 22)
print(len(den))