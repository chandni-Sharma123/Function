# def f():
#     a=int(input("enter number"))
#     b=int(input("enter number"))
#     d=a+b
#     print(d)
# f()



# def f():
#    a=[5,5,15,5,30,7,9,6]
#    i=0
#    sum=0
#    while i<len(a):
#       sum=sum+a[i]
#       if sum%5==0:
#          print(sum,"fghji")
#       else:
#          print(sum,"not")
#       i=i+1
# f()



# def pelindrom():
#    name=""
#    b=name[-1::-1]
#    if (name==b):
#       print(b)
#    else:
#     print("no")
# pelindrom()


# def p():
#    string=input(("Enter a string:"))
#    if(string==string[::-1]):
#       print("The string is a palindrome")
#    else:
#       print("Not a palindrome")
# p()






# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")








# func1=(20,40,60)
# func2=(80,70,100)
# def func():
#     i=0
#     while i<len(func1):
#           j=0
#           while j<len(func2):
#               print(func1[i],func2[j])
#               i=i+1
#               j=j+1
# func()






# list=['aba','xyx','121','345']
# i=0
# count=0
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         if list[i][0]==list[i][-1]:
#             count=count+1
#             break
#         j=j+1
#     i=i+1
# print(count)