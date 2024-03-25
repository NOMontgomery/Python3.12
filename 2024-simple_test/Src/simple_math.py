def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def reverse_str(inp_string: str) -> str:
    return inp_string[:: -1]


if "__main__" == __name__:

    print(f"{reverse_str()} {addition(9, 9)} {substraction(10, 7)}")