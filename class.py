# # Define the class (blueprint) 
# # class Dog:
# #     pass

# # Instantiate object (create actual dogs)
# # my_dog = Dog() # my_dog is now an instance of the Dog class
# # your_dog = Dog()


# # class Dog:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age =age
# #         pass

# # print("==========================================================="+2)

# # class BankAccount:
# #     interest_rate = 0.02
# #     account_count = 0 

# #     def __init__(self, owner, balance):
# #         self.owner = owner
# #         self.balance = balance
# #         BankAccount.account_count += 1


# # my_bank = BankAccount("victor", 100)
# # your_bank = BankAccount("Nathan", 200)
# # your_schools = BankAccount("your school", 300)
# # Family_account = BankAccount("your family", 1000)

# # print("*=*"*87)
# # print("Our bank accounts")
# # print(BankAccount.interest_rate)
# # print(BankAccount.account_count)

# # class BookKeeping:
# #     document = 0.02
# #     document_count = 0

# #     def __init__(self, owner, info):
# #         self.owner = owner
# #         self.info = info
# #         BookKeeping.document_count += 1


# # my_document = BookKeeping("Ethan", 20)
# # your_document = BookKeeping("Olive", 15)

# # print("*=*"*87)
# # print("Our book Keeping record") 
   
# # print(BookKeeping.document)
# # print(BookKeeping.document_count)


# # method in class

# # class person:
# #     population = 0

# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         person.population += 1


# #     @classmethod
# #     def get_population(cls):
# #         return cls.population
    
# #     @classmethod
# #     def from_birth_year(cls, name, birth_year):
# #         import datetime
# #         age = datetime.date.today().year - birth_year
# #         return cls(name, age)   
    
# # class animal:
# #     population = 0

# #     def __init__(self, name, species):
# #         self.name = name
# #         self.species = species
# #         animal.population += 1

# #     @classmethod
# #     def get_population(cls):
# #         return cls.population
    
# #     @classmethod
# #     def from_species(cls, name, species):
# #         return cls(name, species)


# # class Temperature:
# #     def __init__(self, celsius):
# #         self._celsius = celsius

# #     @property
# #     def celsius(self):
# #         """Getter"""
# #         return self._celsius

# #     @celsius.setter
# #     def celsius(self, value):
# #         """Setter with validation"""
# #         if value < -273.15:
# #             raise ValueError("Temperature below absolute zero is not possible.")
# #         self._celsius = value

# #     @property
# #     def fahrenheit(self):
# #         """Computed property — no setter needed"""
# #         return (self._celsius * 9/5) + 32

# # t = Temperature(25)
# # print(t.celsius)      # 25
# # print(t.fahrenheit)   # 77.0

# # t.celsius = 100
# # print(t.fahrenheit)   # 212.0

# # t.celsius = -300      # ❌ Raises ValueError


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def breathe(self):
#         return f"{self.name} breathes air."

#     def speak(self):
#         return f"{self.name} makes a sound."

#     def __str__(self):
#         return f"{self.__class__.__name__}(name={self.name}, age={self.age})"


# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)    # call parent __init__
#         self.breed = breed

#     def speak(self):                   # override parent method
#         return f"{self.name} says: Woof!"

#     def fetch(self):
#         return f"{self.name} fetches the ball!"


# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says: Meow!"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def breathe(self):
#         return f"{self.name} breathes air."

#     def speak(self):
#         return f"{self.name} makes a sound."

#     def __str__(self):
#         return f"{self.__class__.__name__}(name={self.name}, age={self.age})"


# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)    # call parent __init__
#         self.breed = breed

#     def speak(self):                   # override parent method
#         return f"{self.name} says: Woof!"

#     def fetch(self):
#         return f"{self.name} fetches the ball!"


# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says: Meow!"
    
# dog = Dog("Rex", 3, "Labrador")
# cat = Cat("Whiskers", 5)

# print(dog.breathe())   # inherited from Animal
# print(dog.speak())     # overridden in Dog
# print(dog.fetch())     # unique to Dog
# print(cat.speak())     # overridden in Cat
# print(str(dog))        # uses Animal.__str__ → Dog(name=Rex, age=3)


# # # duck
# # class Flyable:
# #     def fly(self):
# #         return f"{self.name} is flying!"

# # class Swimmable:
# #     def swim(self):
# #         return f"{self.name} is swimming!"

# # class Duck(Animal, Flyable, Swimmable):
# #     def speak(self):
# #         return f"{self.name} says: Quack!"

# # donald = Duck("Donald", 2)
# # print(donald.fly())    # from Flyable
# # print(donald.swim())   # from Swimmable
# # print(donald.speak())  # overridden in Duck 


# # class GuideDog(Dog):
# #     def __init__(self, name, age, breed, owner_name):
# #         super().__init__(name, age, breed)   # call Dog.__init__
# #         self.owner_name = owner_name

# #     def speak(self):
# #         parent_speak = super().speak()       # call Dog.speak
# #         return f"{parent_speak} (Guide dog for {self.owner_name})"

# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclasses must implement area()")

#     def describe(self):
#         return f"I am a {self.__class__.__name__} with area {self.area():.2f}"


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         import math
#         return math.pi * self.radius ** 2


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# +

# class work
# from abc import ABC, abstractmethod

# class fish(ABC):
#     """Abstract base class for all fish"""

#     @abstractmethod
#     def habitat(self):
#         """Must be implemented by all fish subclasses"""
#         pass

#     @abstractmethod
#     def diet(self):
#         """Must be implemented by all fish subclasses"""
#         pass

#     def describe(self):
#         """Concrete method — shared by all fish"""
#         return (f"{self.__class__.__name__} | "
#                 f"Habitat: {self.habitat()} | "
#                 f"Diet: {self.diet()}")
    
# class Salmon(fish):
#     def habitat(self):
#         return "Freshwater and Saltwater"

#     def diet(self):
#         return "Insects, small fish, plankton"
# class Trout(fish):
#     def habitat(self):
#         return "Freshwater"

#     def diet(self):
#         return "Insects, small fish, crustaceans"
    
# salmon = Salmon()
# trout = Trout()

# print(salmon.describe())
# print(trout.describe())

# mini project


