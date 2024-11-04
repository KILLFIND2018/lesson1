class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        a = super(House, cls).__new__(cls)
        return a


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self.name)



    def go_to(self, new_floor):
        for i in range(1, new_floor+1):
            new_floor = i
            print(f"{new_floor}")
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
                return

    def __del__(self):
        print(f'"{self.name} снесён, но он останется в истории"')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)