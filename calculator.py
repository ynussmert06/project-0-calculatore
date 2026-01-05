operation = {
      "+": lambda number1, number2: number1 + number2,
      "-": lambda number1, number2: number1 - number2,
      "*": lambda number1, number2: number1 * number2,
      "/": lambda number1, number2: number1 / number2 if number2 != 0 else "ошибка"
   }
try:
    number1 = float(input("первое число: "))
    number2 = float(input("второе число: "))
except ValueError:
    print("введено не число, остановка")
    exit()
function = input("действия: +, -, *, /, end: ")
while function != "end":
    if function in operation:
        otvet = operation[function](number1, number2)
        print(otvet)
        if otvet == "ошибка":
            break
        user_otvet = input("продолжить работу с ответом? y/n: ")
        if user_otvet == "y":
            try:
                new_number2 = float(input("введите второе число: "))
                number1 = otvet
                number2 = new_number2
                function = input("действия: +, -, *, /, end: ")
            except ValueError:
                print("введено не число, остановка")
                break
        else:
            break
print("end while")

