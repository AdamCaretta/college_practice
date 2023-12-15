def fun_1(num, dom):
    try:
        v = num / dom
        print(f"{num} / {dom} = {v}")
        return v
    except ZeroDivisionError as e:
        print(f"You cannot divide {num} by 0!")
        return "UNKNOWN"
    finally:
        print("Finally code in fun_1")


def fun_0(num):
    try:
        if not isinstance(num, str):
            raise TypeError(
                f"The argument num must be a str {type(num).__name__} was received."
            )
        if not num.replace(".", "").replace("-", "").isnumeric():
            raise ValueError(f"{num} cannot be converted to a number.")
        num = int(num)
        v = fun_1(num + 1, num - 1)
        print(f"fun_1 result: {v}")
    finally:
        print("Finally code in fun_0")


if __name__ == "__main__":
    while True:
        try:
            ui = input("Input: ")
            fun_0(ui)
        except (TypeError, ValueError) as e:
            msg = str(e)
            print(e)
    print("finished invoking fun_0")
