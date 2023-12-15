def enter_num():
    user_input = input("Input a numerical value: ")
    user_float = float(user_input)
    return user_float


def math():
    num1 = enter_num()
    math_operator = input("/, *, -, or +: ")
    num2 = enter_num()

    if math_operator == "+":
        return num1 + num2
    elif math_operator == "-":
        return num1 - num2
    elif math_operator == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Can't divide by 0, try again")
            math()
    elif math_operator == "*":
        return num1 * num2
    else:
        print("Please enter a valid operator /, *, -, or +:")
        math()


print(math())
