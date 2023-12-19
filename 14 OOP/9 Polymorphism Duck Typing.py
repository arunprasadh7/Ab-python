# POlymorphism - many forms - one name many actions

def driver(car):
    car.drive()

class Creta:
    def drive(self):
        print('Driving a creta.')

class Tesla:
    def drive(self):
        print('Driving a Tesla.')

c1 = Creta()
driver(c1)

t1 = Tesla()
driver(t1)


# Duck example

def pet_lover(pet):
    pet.talk()
    if hasattr(pet,'walk'):
        pet.walk()


class Duck:
    def talk(self):
        print('Duck is quacking')

    def walk(self):
        print('Duck is walking')

class Dog:
    def talk(self):
        print('This dog is barking')

    # def walk(self):
    #     print('This dog is walking')

duck1 = Duck()
pet_lover(duck1)

dog1 = Dog()
pet_lover(dog1)


duck2 = Dog()
pet_lover(duck2)