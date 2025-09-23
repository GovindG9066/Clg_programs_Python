print("Sept-23")

print("5 Example of If-Else statement : ")
# 1
x=10
y=5
if x==y:
    print("Same")
else:
    print("Not same")

# 2
age=15
if age >= 18:
    print("You are eligibal for lincence")
else:
    print("You are not eligibal for lincence")
 
 # 3
a=10
if a % 2==0:
    print(a," is even")
else:
    print(a," is odd")

# 4
a=5
if a > 5:
    print(a," is greate than 5")
else:
    print(a," is not greater than 5")

# 5
x=int(input("Enter a number : "))

if x > 0:   
    print(x," is positive number")
elif x < 0:
    print(x," is negative number")
else:
    print(x," is Zero")

print("for loop : ")

# 1
a=int(input("Enter a number : "))

for i in range(a,a+11):
    print(i)

# 2 
a=int(input("Enter a number : "))
for i in range(a,a*10+1):
    if i % a == 0:
        print(i)

# 3
num=6

for i in range(num,num*10+1,num):
    print(i)

# 4

num=7
isture=False

for i in range(1,num):
    if num % i != 0:
        istrue=True
    else:
        istrue=False
if istrue==True:
    print(num," is prime")
else:
    print(num," not a prime number")

# 5

num=9
for i in range(1,num+1):
    if num % i==0:
        print(i)


