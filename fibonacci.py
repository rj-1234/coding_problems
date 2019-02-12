"""
Recursion without meoization
"""
# def fibonacci(n):
#     l = [0, 1]

#     if n < 2:
#         return l[n]
    
#     return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(5))

"""
Recursion with memoization
"""
alist = []

def fibonacci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    if alist[number] != -1:
        return alist[number]
    else:
        alist[number] = fibonacci(number-1)+fibonacci(number-2)
        return alist[number]

def main():
    n = int(input('enter the no. of elements in the fibonacci series : '))
    for i in range(0, n+1):
        alist.append(-1)

    val = fibonacci(n)
    print(val)


if __name__ == "__main__": main()