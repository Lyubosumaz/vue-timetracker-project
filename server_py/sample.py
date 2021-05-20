# 1
class Dog():
    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


# my_dog = Dog(breed='Lab', name="Sammy")
my_dog = Dog('Lab', "Sammy")
# other_dog = Dog(breed='Husky')
# print(other_dog.breed)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)


# 2
class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


my_c = Circle(3)
my_c.set_radius(99)
print(my_c.area())


# 3
# INHERITANCE
class Animal():
    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('ANIMAL')

    def eat(self):
        print('EATING')


mya = Animal()
mya.who_am_i()
mya.eat()


class Dog(Animal):
    def __init__(self):
        # super().__init__()
        # Animal.__init__(self)
        print('DOG CREATED')

    def bark(self):
        print('WOOF')


myd = Dog()
myd.who_am_i()
myd.eat()
myd.bark()


# SPECIAL METHODS
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'Title: {}, Author: {}, Pages: {}'.format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('a book is destroyed!')


b = Book('Python', 'Jose', 200)
print(b)
print(len(b))
del b

my_list = [1, 2, 3]
print(my_list)
