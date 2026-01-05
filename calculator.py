
number1 = float(input("первое число: "))
number2 = float(input("второе число: "))
function = input("действия: +, -, *, /, end: ")
while function != "end":
    if function == "+":
        otvet = number1 + number2
        print(otvet)
        number1 = otvet
        user_otvet = input("продолжить действия с ответом? y/n ")
        if user_otvet == "y":
            new_number2 = float(input("второе число "))
            number2 = new_number2
            function = input("действия: +, -, *, /, end: ")
        else:
            break
    if function == "-":
        otvet = number1 - number2
        print(otvet)
        number1 = otvet
        user_otvet = input("продолжить действия с ответом? y/n ")
        if user_otvet == "y":
            new_number2 = float(input("второе число "))
            number2 = new_number2
            function = input("действия: +, -, *, /, end: ")
        else:
            break
    if function == "*":
        otvet = number1 * number2
        print(otvet)
        number1 = otvet
        user_otvet = input("продолжить действия с ответом? y/n ")
        if user_otvet == "y":
            new_number2 = float(input("второе число "))
            number2 = new_number2
            function = input("действия: +, -, *, /, end: ")
        else:
            break
    if function == "/":
        try:
            otvet = number1 / number2
            print(otvet)
            number1 = otvet
            user_otvet = input("продолжить действия с ответом? y/n ")
            if user_otvet == "y":
                new_number2 = float(input("второе число "))
                number2 = new_number2
                function = input("действия: +, -, *, /, end: ")
            else:
                break
        except ZeroDivisionError:
            print("деление на 0, конец цикла")
            break
print("end while")

