# 4 - oy 4 - dars
print("Hello World")

def calculate(a:int, b:int):
    return a+b
print(calculate(5,4))


class Employee:
    def __init__(self,name,lastname,salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary


print("salom dunyo")

print(" bu papakada faylar haqida to'liq malumot berilgan")
print (" bu papaka da bu  fyal haqida to'liq malumot berilgan ")
# homeworks
# Descriptor oid masalalar
# 1 masala
class LowercaseDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Qiymat matn bo'lishi kerak")
        instance.__dict__[self.name] = value.lower()

    def __set_name__(self, owner, name):
        self.name = name

class ExampleClass:
    lowercase_value = LowercaseDescriptor()

obj = ExampleClass()
obj.lowercase_value = "HELLO"
print(obj.lowercase_value)
#-------------------------------------------------
# 2 masala
class PositiveValueDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Qiymat musbat bo'lishi kerak")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class AnotherExampleClass:
    positive_value = PositiveValueDescriptor()

example = AnotherExampleClass()
example.positive_value = 10
print(example.positive_value)
#---------------------------------------------------------
# Datetime Moduli oid masalalar
# 1 masala
from datetime import datetime, timedelta

today = datetime.now()
plus_seven_days = today + timedelta(days=7)
minus_seven_days = today - timedelta(days=7)
print(f"Bugungi sana: {today}")
print(f"7 kun keyin: {plus_seven_days}")
print(f"7 kun oldin: {minus_seven_days}")
#----------------------------------------------
# 2 masala
birth_year = int(input("Tug'ilgan yilingizni kiriting: "))
today = datetime.now()
current_year = today.year
age = current_year - birth_year
if today.month == 1 and today.day == 1:
    print("Tug'ilgan kuningiz bilan!")
else:
    print(f"Sizning yoshingiz: {age}")
#------------------------------------------------------------------------
# 3 masala
start_time = datetime(2024, 12, 10, 12, 0, 0)
end_time = datetime(2024, 12, 10, 14, 30, 0)
total_seconds = (end_time - start_time).total_seconds()
print(f"Jami soniyalar: {total_seconds}")


# Math Moduli oid masalar
#1 masala
import math

diameter = float(input("Aylana diametrini kiriting: "))
radius = diameter / 2
area = math.pi * (radius ** 2)
print(f"Aylana yuzasi: {area}")
#-------------------------------------------
# 2 misol
number = float(input("Sonni kiriting: "))
if number < 0:
    raise ValueError("Son musbat bo'lishi kerak")

square_root = math.sqrt(number)
cube_root = number ** (1/3)
print(f"Kvadrat ildiz: {square_root}")
print(f"Kub ildiz: {cube_root}")
#-------------------------------------------------------------
# Random Moduli: Tasodifiy sonlar
# 1 masala
import random

integers = [random.randint(1, 100) for _ in range(5)]
real_numbers = [random.random() for _ in range(3)]

average = (sum(integers) + sum(real_numbers)) / (len(integers) + len(real_numbers))
print(f"Tasodifiy butun sonlar: {integers}")
print(f"Tasodifiy haqiqiy sonlar: {real_numbers}")
print(f"O'rtacha qiymat: {average}")




