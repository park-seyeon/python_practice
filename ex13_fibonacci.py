def fibonacci():
    num = int(input("How many fibonaccis?: "))
    list = []
    x = 0
    y = 1
    for i in range(num):
        z = x + y
        x = y
        y = z
        list.append(x)
    return list


print(fibonacci())

# from SOLUTION


def fib_solution():
    num = int(input("How many fibonaccis?: "))
    if num == 1:
        fib = [1]
    elif num == 2:
        fib = [1, 1]
    else:
        i = 1
        fib = [1, 1]
        while i < num - 1:
            fib.append(fib[i-1]+fib[i])
            i += 1
    return fib


print(fib_solution())
