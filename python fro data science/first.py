# a = 12
# b = 13 
# c = float(a) + float(b)
# # print(c)

# # list
# mylist = [1,2,3,4,5]

# #methods list 

# # append
# mylist.append(7)
# print(*mylist)

# # insert 
# mylist.insert(2,6)
# print(*mylist)

# #remove
# mylist.remove(6)
# print(*mylist)

# #pop 
# mylist.pop()
# print(*mylist)

# #sort
# mylist2 = [2,3,5,4,1]
# print(*mylist2)
# mylist2.sort()
# print(*mylist2)

# #reverse
# mylist.reverse()
# print(*mylist)

#conditions
# a = 15 
# b = 14

# if(a > b) :
#     print("a is bigger")
# elif(a < b) :
#     print("b is bigger")
# else :
#     print("a and b are equal")

# function
# def sum(a,b) :
#     return a + b

# print(sum(9,3))

# def printList(mylist) :
#     print(mylist)

# def sortList(mylist) :
#     return mylist.sort()

# list = [9,8,7,6,5]
# printList(list)
# sortList(list)
# printList(list)

#exceptioon handing
# try :
#     num = int(input("Enter a number : "))
#     result = 10 / num
# except ValueError :
#     print("Value Error")
# except ZeroDivisionError :
#     print("cannot divide by zero")
# else :
#     print(f"result is {result}") #f is used for print float
# finally :
#     print("execution completed")

#dictonary
# mydict = {"age" : 12, "Name" : "Aman"}
# mydict["email"] = "abc@gmail.com"
# for key,value in mydict.items() :
#     print(f"{key} : {value}")

# del mydict["email"]
# for key,value in mydict.items() :
#     print(f"{key} : {value}")

# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())
# print(mydict.clear())

# newdict = {
#     "name" : "Arun",
#     "Age" : 19
# }

# mydict.update(newdict)
# print(mydict.items())

#problem 1
# str = input("enter a string :")
# reverseStr = str[::-1]
# print(reverseStr)

#problem 2
# num = int(input("enter a number : "))
# for i in range(2,int(num ** 0.5) + 1) :
#     if(num % i == 0) :
#         print("not a prime number")
#     else :
#         print("a prime number")

#problem 3
# list = [2,4,6,3,5]
# a = 0
# for i in list :
#     if(a < i) :
#         a = i

# print(a)

# problem 4 
# str = input("enter a string :")
# reverseStr = str[::-1]

# if(str == reverseStr) :
#     print(f"{str} is palindrome")
# else :
#     print(f"{str} is not palindrome")

# problem 5
# def factorial(num) :
#     if(num == 0) :
#         return 1
    
#     return num * factorial(num-1)

# print(factorial(4))

# problem 6 
# list1 = [1,2,3]
# list2 = [4,5,6]

# list3 = list1 + list2
# print(*list3)

#problem 7
num = int(input("Enter a number : ")) 
for i in range(2,num) :
    for j in range(2,int(i ** 0.5) + 1) :
        if(i % j == 0) :
           break
    else :
        print(i , end=" ")
       
    