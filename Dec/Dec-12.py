# print("1. Factorial of the number :")

# def facto(num):
#     if num == 1:
#         return 1
#     return num*facto(num-1)

# print(facto(5))

# 2 sum of square of first n natural num
# print("2. sum of square of first n natural number :")

# def sum_of_squares(num):
#     if num == 1:
#         return 1
#     return (num**2) + sum_of_squares(num-1)

# print(sum_of_squares(5))

# def average():
#     count=int(input("Enter a count :"))
#     l1=[]
#     for i in range(1,count+1):
#         a=int(input("Enter a num :"))
#         l1.append(a)
#     print(l1)
#     return (sum(l1)/(count))

# print("Average is :",average())

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

# num=lambda x:x*5
# for i in range(1,11):
#     print(num(i))

# print("Function for prime no or not :")

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

# def removevowels(userinput):
#     print("User input :",userinput)
#     vowels="aeiouAEIOU"
#     result=""

#     for char in userinput:
#         if char not in vowels:
#             result+=char
#     return result
# print("User input without vowels :",removevowels("Govind"))

# def Char_at_even_index(userinput):
#     result=""
#     print("Initially :",userinput)
#     for i in range(len(userinput)):
#         if i % 2 == 0:
#             result+=userinput[i]
            
#     print("After remove :",result)

# Char_at_even_index("Govind")

# print("URL validation...")
# import re

# URL="https://www.google.com"
# pattern=r"^https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

# if re.match(pattern,URL):
#     print("Valid URL")
# else:
#     print("Invalid URL")

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

# print("Fib series using yield keyword :")

# def fibseries(n):
#     a,b=0,1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
# for num in fibseries(10):
#     print(num)

# print("Mearged 2 dict :")

# dict1={"a":"Govind","Age":21}
# dict2={"Dist":"Pune","State":"Maharashtra"}

# dict1.update(dict2)
# print(dict1)

# print("Return True if any num is duplicate in the list else return false :")
# def same_element():
#     list3=[1,2,5,4,6,1]
#     if list3[0] == list3[-1]:
#         return True
#     return False
# print(same_element())

# print("16. create tuple; print num which is divisibal by 5")

# tup=(12,45,86,4,6,8,2,15,354,3554,61,74)
# print(tup)

# for item in tup:
#     if item % 5 == 0:
#         print(item)

# print("17. comphihension of list,set,tup,dict")

# l1=[i for i in range(1,5) if i % 2 == 0]
# print("List Comprihension")
# print(l1)

# tup1=tuple(num for num in range(2,15,2))
# print("tuple Comprihension")
# print(tup1)

# set1={x for x in range(9,91) if x % 9 == 0}
# print("Set Comprihension")
# print(set1)

# dict01={x:x for x in range(1,10) if x % 2 == 0}
# print("Dict Comprihension")
# print(dict01)


# 18.demonstrate the list dict tup set
# print("demonstrate the list dict tup set")

# list1=[1,2,4,5,5,7]
# tup1=(1,2,4,5,5,7)
# set1={1,2,4,5,5,7}
# dict1={1:2,4:5,5:7}

# print(f"List:{list1}")
# print(f"tuple:{tup1}")
# print(f"Set:{set1}")
# print(f"Dict:{dict1}")

# 19. custom exception handling
# print("19. custom exception handling")

# try:
#     f1=int(input("Enter first num :"))
#     f2=int(input("Enter second num :"))

#     result=f1/f2

#     if f2 == 0:
#         raise ZeroDivisionError
   
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError as zero:
#     print("Divisible by Zero is not possible")

# print("20. Write a python program to demonstrate single tasking handle byone thread.")
# import threading

# def task():
#     for i in range(1, 6):
#         print("Executing task:", i)

# t1 = threading.Thread(target=task)

# t1.start()

# t1.join()

# print("Single task completed")

# print("21. Armstrong number program")
# num=153
# temp=num
# res=0
# while temp:
#     digit=temp % 10
#     res=res+digit**3
#     temp=temp//10
# if res==num:
#     print(num,"is an Armstron Num")
# else:
#     print(num,"is not an Armstron Num")

# print("22. Write a python program to find all prime factors of a number.")
# num = int(input("Enter a number: "))

# print("Prime factors are:")

# i = 2
# while i <= num:
#     if num % i == 0:
#         print(i)
#         num = num // i
#     else:
#         i = i + 1

# print("23. Perfect Number")

# num=28
# lst01=[]
# for i in range(1,num):
#     if num % i == 0:
#         lst01.append(i)

# sum1=sum(lst01)

# if sum1 == num:
#     print(num," is Perfect num")

# print("14.Write a multithreading program, where one thread prints square of a number and another thread prints factorial of a number. Also display the total time taken for the execution.")
# import threading
# import time
# import math

# def square(num):
#     print("Square of", num, "is:", num * num)
#     time.sleep(1)

# def factorial(num):
#     print("Factorial of", num, "is:", math.factorial(num))
#     time.sleep(1)

# num = 5

# # record start time
# start_time = time.time()

# # create threads
# t1 = threading.Thread(target=square, args=(num,))
# t2 = threading.Thread(target=factorial, args=(num,))

# # start threads
# t1.start()
# t2.start()

# # wait for threads to complete
# t1.join()
# t2.join()

# # record end time
# end_time = time.time()

# print("Total time taken:", end_time - start_time, "seconds")

# print("25. Number pattern")

# count=5
# for i in range(1,count+1):
#     print(f"{i} " * i)

# 26. Star Pattern (Simple Right Angle Triangle)
# print("26. Star Pattern (Simple Right Angle Triangle)")
# count=5
# for i in range(1,count+1):
#     print("* " * i)

# 27. Number pattern 1,12,123,1234 etc
# print("Number pattern 1,12,123,1234 etc")

# count=5
# for i in range(1,count+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 28. number pattern like 1,23,456,78910
# print("Number pattern :")

# count=4
# num=1
# for i in range(1,count+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()

# print(" 29. up side down right angle triange")

# count=5
# for i in range(1,count+1):
#     print("* " * (count+1-i))

# 30. Star Pattern (Triangle pattern with diagonal)
# print("30. Star Pattern (Triangle pattern with diagonal)")

# count=5
# for i in range(1,count+1):
#     print("  " * (count-i) + "* " * i + "* " * (i-1))

# print("Multiple inheritance:")
# class dog:
#     def sound(self):
#         return "Brak"
# class cat:
#     def properties(self):
#         return "Having a 4 leg and with different colors"

# class Animal(dog,cat):
#     def features(self):
#         return "different bread,color,sound"
    
# a=Animal()
# print(a.sound())
# print(a.properties())
# print(a.features())

# print("32. Multiplication table from 1-10")

# for i in range(1,11):
#     print("Multiplication table of : ",i)
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")

print("33. even number form list :")

even_num_list=[75,8,89565,89,55,895,8598,524,865,5454,55]

for i in even_num_list:
    if i % 2 == 0:
        print(i)