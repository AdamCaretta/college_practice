def fun_1(num, dom):
    try:
        v = num / dom
        print(f"{num} / {dom} = {v}")
        return v
    except Exception as e:
        print(f"You cannot divide {num} by 0!")
        return "UNKNOWN"


def fun_0(num):
    v = fun_1(num + 1, num - 1)
    print("finished invoking fun_1")


if __name__ == "__main__":
    fun_0(10)
    print("finished invoking fun_0")


try:
    # code that might raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except (ZeroDivisionError, ValueError):
    print("Invalid input!")
