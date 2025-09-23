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

print("While loop : ")

# 1
count=10
num=1
while num != count+1:
    print(num," Hello")
    num+=1 

# 2
count=5
while count != 0:
    print("* " * count)
    count-=1
    

# 3
num=1
count=5
while num <= count:
    print("* " * num)
    num+=1

# 4
num=0
count=5
while count > 0:
    print("  " * num + "* " * count )
    num+=1
    count-=1

# 5
num=int(input("Enter a number : "))
count=1
while count <= 10 :
    print(num," * ",count," = ",count*num )
    count+=1

print("function 5 Example :")
# 1
def addition(a,b):
    return a+b

x=int(input("Enter the 1st number : "))
y=int(input("Enter a 2nd number : "))
z=addition(x,y)
print(z)

# 2nd
def fib(a,b,num):
    if num == 0:
        return
    z=a+b
    print(z)
    
    fib(b,z,num-1)

a=0
b=1
count=10
print(a)
print(b)
fib(a,b,count-2)

# 3rd

def table(num):
    for i in range(1,10+1):
        print(num*i)

table(5)


# 4th

def evenodd(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

evenodd(17)

# 5th

def seriesofeven(num,count):
    if count==0:
        return
    if num % 2 == 0:
        print("Even numbers are : ")
        print(num)
        
    else:
        print("Odd Numbers are : ")
        print(num)
        

    seriesofeven(num+1,count-1)

seriesofeven(1,11)

print("Identifires 5 Example :")

name="Govind"
_age=21
clg_name="VIIT Baramati"
myAddress="A/P Yenere,Tell Junnar, Dist pune"
rollNo123=18

print("List in python :")

mylist=[7,8,6,7,84,52]
print(mylist)
mylist.append(4)
print(mylist)
