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

# def currprevsum(count):
#     l1=[]
#     for i in range(1,count+1):
#         num=int(input("Enter a num :"))
#         l1.append(num)
#     print("Initial List :",l1)
#     prev=0
#     l2=[]
#     for curr in l1:
#         sum=curr+prev
#         prev=curr
#         l2.append(sum)
#     print("List with sum :",l2)

# count=int(input("Enter a count :"))
# currprevsum(count)

# 6 prime num function
print("Function for prime no or not :")

# def primeno(num):
#     prime=True
#     for i in range(2,num):
#         if num % i == 0:
#             prime = False
#     if prime == True:
#         print(f"The num {num} is Prime ")
#     else:
#         print(f"The num {num} is Not Prime")

# primeno(19)

# 7 get input string from user and delete the vowels from the string and print it again
print("7. input string from user and remove the vowels from string :")

def removevowels(userinput):
    print("User input :",userinput)
    vowels="aeiouAEIOU"
    result=""

    for char in userinput:
        if char not in vowels:
            result+=char
    return result
print("User input without vowels :",removevowels("Govind"))

# 8.accept the string from the user print char which is present on the even index
print("accept the string from the user and print the char on the even index :")

def Char_at_even_index(userinput):
    result=""
    print("Initially :",userinput)
    for i in range(len(userinput)):
        if i % 2 == 0:
            result+=userinput[i]
            
    print("After remove :",result)

Char_at_even_index("Govind")

#2nd small version
print("This is the simple version,One line code :")
n="Govind"
print(n[::2])

# 9.Valid URL 
print("URL validation...")
import re

URL="https://www.google.com"
pattern=r"^https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.match(pattern,URL):
    print("Valid URL")
else:
    print("Invalid URL")

# Exception Handling
print("Exception Handling :")

try:
    file=open("file.txt","r")
except FileNotFoundError as e:
    print("404 error file Not Found")
    
    #or

# try:
#     first=int(input("Enter a first num :"))
#     second=int(input("Enter a second num :"))

#     result=first/second
#     print(result)
# except ValueError:
#     print("Enter the correct Integer input")
# except ZeroDivisionError:
#     print("Divide by Zero is not possible")
# except:
#     print("Other error")

# 13. fib series using yield keyword
print("Fib series using yield keyword :")

def fibseries(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in fibseries(10):
    print(num)


# 14. mearge 2 dict
print("Mearged 2 dict :")

dict1={"a":"Govind","Age":21}
dict2={"Dist":"Pune","State":"Maharashtra"}

dict1.update(dict2)
print(dict1)

# 15. return true if first and last element is same
print("Return true if first and last element is same else return false :")

# def same_element():
#     list3=[1,2,5,4,6,1]
#     if list3[0] == list3[-1]:
#         return True
#     return False
# print(same_element())

# 2nd

def same_element(lst):
    return lst[0] == lst[-1]
print(same_element([12,15,35,45,96,12]))
print(same_element([12,15,35,45,96,1]))

