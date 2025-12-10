print("Dec 10")
print("Practical question :")
#fib

def fib(first,second,n):
    if n is 0:
        return
    sum=first+second
    print(first)
    fib(second,sum,n-1)

fib(0,1,10)


# 1 factorial of the num
print("Factorial of the number :")

def facto(num):
    if num == 1:
        return 1
    return num*facto(num-1)

print(facto(5))

