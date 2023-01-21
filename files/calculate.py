print("Введите число")
number_1 = input()

while number_1.isnumeric() == False:
    print("Вы ввели не число! Введите число: ")
    number_1 = input()

print("Введите знак")
operator = input()


print("Введите число")
number_2 = input()

while number_2.isnumeric() == False:
    print("Вы ввели не число! Введите число")
    number_2 = input()


def addition(number_1, number_2):
    """"Функция сложения"""
    result = int(number_1) + int(number_2)
    print("Сумма переменных равна: " + str(result))

def subtraction(number_1, number_2):
    """"Функция вычитания"""
    result = int(number_1) - int(number_2)
    print("Разность переменных равна: " + str(result))

def multiplication(number_1, number_2):
    """"Функция умножения"""
    result = int(number_1) * int(number_2)
    print("Произведение переменных равно: " + str(result))

def division(number_1, number_2):
    """"Функция деления"""
    try:
        result = int(number_1) / int(number_2)
        print("Частность переменных равна: " + str(result))
    except ZeroDivisionError:
        print("На ноль делить нельзя!")

if operator == "+":
    addition(number_1, number_2)
elif operator == "-":
    subtraction(number_1, number_2)
elif operator == "*":
    multiplication(number_1, number_2)
elif operator == "/":
    division(number_1, number_2)
