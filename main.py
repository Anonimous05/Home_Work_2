num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

operation = input("Выберите оперцию: \n + \n - \n * \n / \n % \n // \n ** \n")

if operation == "+":
    print("Вы выбрали сложение: " + str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
elif operation == "-":
    print("Вы выбрали вычитание: " + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
elif operation == "*":
    print("Вы выбрали умножение: " + str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
elif operation == "/":
    print("Вы выбрали деление: " + str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
elif operation == "%":
    print("Вы выбрали остаток от деление: " + str(num1) + " % " + str(num2) + " = " + str(num1 % num2))
elif operation == "//":
    print("Вы выбрали целочисленное деление: " + str(num1) + " // " + str(num2) + " = " + str(num1 // num2))
elif operation == "**":
    print("Вы выбрали возведение в степень: " + str(num1) + " ** " + str(num2) + " = " + str(num1 ** num2))
else:
    print("Выберите оперцию из выше перечисленных!")