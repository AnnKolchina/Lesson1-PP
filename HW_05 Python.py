'''5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
    нужно использовать методы get и set'''

class Animal:

    count_animal = 0
    __owner = 'Zoo'

    def __init__(self, type_an, kind, name):
        self.type_an = type_an
        self.kind = kind
        self.name = name

    def alive(self, move):
        if move:
            return f'{self.name} is alive!'
        else:
           return f'{self.name} is not alive!'

    def my_str(self):
        return f'{self.type_an} {self.kind} {self.name}'

    def get_owner(self):
        return self.__owner

    def set_owner(self, new_owner):
        self.__owner = new_owner




class Cat(Animal):
    def __init__(self, type_an, kind, name, color):
        super().__init__(type_an, kind, name)
        self.color = color

    def my_str_cat (self):
        return f'{self.my_str()} {self.color}'

class Dog(Animal):
    def __init__(self, type_an, kind, name, high):
        super().__init__(type_an, kind, name)
        self.high = high





cat_1 = Cat('mlek', 'cats', 'Black', 'white')

print(cat_1.my_str_cat())
animal_1 = Animal('pozv', 'fishs', 'Fed')
print(animal_1.get_owner())
animal_1.set_owner('Ann')
print(animal_1._Animal__owner)
print(animal_1.get_owner())

