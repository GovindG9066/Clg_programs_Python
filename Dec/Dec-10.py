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
print("1. Factorial of the number :")

def facto(num):
    if num == 1:
        return 1
    return num*facto(num-1)

print(facto(5))

# 2 sum of square of first n natural num
print("2. sum of square of first n natural number :")

def sum_of_squares(num):
    if num == 1:
        return 1
    return (num**2) + sum_of_squares(num-1)

print(sum_of_squares(5))

# 3 create fu average() which will return the average of the number input by user

# def average():
#     num=input("Enter the number of list with space :")

#     l1=list(map(float,num.split()))

#     return (sum(l1)/len(l1))

# print("The Average is ",average())

# def average():
#     count=int(input("Enter a count :"))
#     l1=[]
#     for i in range(1,count+1):
#         a=int(input("Enter a num :"))
#         l1.append(a)
#     print(l1)
#     return (sum(l1)/(count))

# print("Average is :",average())
        
# iteration n number and print the sum of current and previous num
print("iterate the n numbers & print the sum of current and previous number :")

def currprevsum(count):
    l1=[]
    for i in range(1,count+1):
        num=int(input("Enter a num :"))
        l1.append(num)
    print("Initial List :",l1)
    prev=0
    l2=[]
    for curr in l1:
        sum=curr+prev
        prev=curr
        l2.append(sum)
    print("List with sum :",l2)

count=int(input("Enter a count :"))
currprevsum(count)

    