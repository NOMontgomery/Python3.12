def my_multiplication(x, y):
    zero = 0
    math = 0
    # while math < y:
    #     zero += x
    #     math += 1
    for v in range(y):
        zero += x

    return zero


def my_divison(u, z):
    goal = 0

    for c in range(z):
        goal -= u
        return goal


print(my_multiplication(5, 3))
print(my_divison(20, 10))


def my_function(*kids):
    print("The youngest child is " + kids[len()])


my_function("Emil", "Tobias", "Linus")
