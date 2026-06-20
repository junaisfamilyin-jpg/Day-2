# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def introduce(self):
#         print(f"Hi, my name is {self.name}, I am {self.age} years old.")

#     def is_passing(self):
#         return self.grade >= 50

# student1 = Student("Ali", 16, 82)

# student1.introduce()

# print(student1.is_passing())





# class bank_account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount

#     def withdrawl(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount

#         else:
#             print("Not enough money in the account!")

#     def display_balance(self):
#         print(f"{self.owner} has {self.balance} in their account.")

# account1 = bank_account("Sara", 500)
# account1.deposit(200)
# account1.withdrawl(100)
# account1.display_balance()



# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.speed = 0

#     def accelerate(self, amount):
#         self.speed += amount

#     def brake(self, amount):
#         if self.speed - amount >= 0:
#             self.speed -= amount
#         else:
#             self.speed = 0

#     def display_speed(self):
#         print(f"The {self.brand} {self.model} is going {self.speed} km/h")


# car1 = Car("Toyota", "Camry", 2020)

# car1.accelerate(50)
# car1.brake(20)
# car1.display_speed()


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_available = True

#     def borrow(self):
#         if self.is_available == True:
#             self.is_available = False
#             print("You borrowed the book.")
#         else:
#             print("This book is already borrowed.")

#     def return_book(self):
#         self.is_available = True
#         print("You returned the book.")

#     def display_info(self):
#         print(f"{self.title} by {self.author} - Available: {self.is_available}")


# book1 = Book("Harry Potter", "J.K. Rowling")

# book1.display_info()
# book1.borrow()
# book1.borrow()
# book1.return_book()
# book1.display_info()


