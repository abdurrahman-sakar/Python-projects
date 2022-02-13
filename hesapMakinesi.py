# CALCULATOR PROJECT

class calc(object):
    "calculator"

    def __init__(self, a, b):    # init metodu
        "initiialize values"
        self.value1 = a
        self.value2 = b

    def add(self):
        return self.value1 + self.value2

    def subtraction(self):
        return self.value1 - self.value2

    def multiply(self):
        return self.value1 * self.value2

    def division(self):
        return self.value1 / self.value2

"""
[1] Add
[2] Multiply
[3] Subtraction
[4] Division

"""
selection = input("CHOOSE\n Add(1)\n Multiply(2)\n Division(3)\n Subtraction(4) ")

a = float(input("first number: "))
b = float(input("second number: "))

v1 = a
v2 = b
calculator1 = calc(v1,v2)   # created calculator1



if selection == "1":
    result1 = calculator1.add()
    print("Add: ", result1)
elif selection == "2":
    result2 = calculator1.multiply()
    print("Subtruction: ", result2)
elif selection == "3":
    result3 = calculator1.division()
    print("Multiply: ", result3)
elif selection == "4":
    result4 = calculator1.subtraction()
    print("Division: ", result4)
else:
    print("Please, Try Again")






