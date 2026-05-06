# 1-m
class Car:
    def __init__(self,brand, year, speed, fuel):
        self.brand = brand
        self.year = year
        self._speed = speed
        self.__fuel = fuel

    def accelerate(self,x):
        self._speed += x


    def refuel(self,x):
        self.__fuel += x

    def show_info(self):
        print(f'brand:{self.brand}')
        print(f'year:{self.brand}')
        print(f'speed:{self._speed}')
        print(f'fuel:{self.__fuel}')



car1 = Car("BMW", 2020, 100, 50)
car1.accelerate(20)
car1.refuel(10)
car1.show_info()


# 2-m
class Student:
    def __init__(self,name, age, _grade, __password):
        self.name = name
        self.age = age
        self._grade = grade
        self.__password = password


    def study(self,hours):
      self._grade += hours

    def check_password(self,pw):
       self.__password == pw

    def info(self):
        print(f'name:{self.name} Grade:{self._grade}')



a= Student('Ali',18,70,'1234')
a.study(10)


print(ali.info())
print(ali.check_password("1234"))
print(ali.check_password("0000"))


# 3-m
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def deposit(self, x):
        self._balance += x

    def withdraw(self, pin, x):
        if pin != self.__pin:
            print("Wrong pin")
        elif x > self._balance:
            print("Not enough money")
        else:
            self._balance -= x

    def check_balance(self):
        print(self._balance)



acc = BankAccount("Ali", 100, 1234)

acc.deposit(50)
acc.check_balance()

acc.withdraw(1111, 50)
acc.withdraw(1234, 50)
acc.check_balance()

# 4-m
class Phone:
    def __init__(self,model, _battery, __imei):
        self.model = model
        self._battery = _battery
        self.__imei = __imei

    def call(self,minutes):
        self._battery -= minutes


    def charge(self, x):
        self._battery += x


    def info(self):
        print(f'Battery:{self._battery}')

phone1 = Phone("iPhone", 100, "123456789")

phone1.call(20)
phone1.info()

phone1.charge(20)
phone1.info()

# 5-m
class Book:
    def __init__(self, title, author, _pages, __code):
        self.title = title
        self.author = author
        self._pages = _pages
        self.__code = __code

    def read(self, pages):
        print(f"Reading {pages} pages")

    def bookmark(self, page):
        if page > self._pages:
            print("Xato: sahifa kitobdan katta!")
        else:
            print(f"Bookmark at {page}")

    def info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self._pages}")
