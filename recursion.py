# sum of 1 to n (using recursion)

# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return (n+sum(n-1))
# n=int(input("enter number"))
# c=sum(n) 
# print(c)




# string and power Value
# print the string in reverse order using Recursion



# def value(s,n):
#     if n==0:
#         print(s[0]) 
#     else:
#         print(s[n],end="")
#         value(s,n-1)
# s=input("enter name")
# value(s,len(s)-1)




# x to the power y using recursion


# def find(x,y):
#     if y==0:
#         return 1
#     else:
#         return (x*find (x,y-1))
# x=int(input ("enter no."))
# y=int(input ("enter no."))
# s=find(x,y)
# print(s)




# find factorial Using Recursion

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return(n*fact (n-1))
# n=int(input("enter number"))
# z=fact(n)
# print(z)






# def demo(a,b):
#     c=a+b
#     print("add=",c)
#     demo1(5,3)
# def demo1(h,g):
#     d=h+g
#     print(d)
# demo(2,3)






# def s(n):
#     x=0
#     y=1
#     z=0
#     while z<=n:
#         print(z)
#         x=y
#         y=z
#         z=x+y
# n=int(input("enter no."))
# s(n)












# def f(n):
#    if n <= 1:
#        return n
#    else:
#        return(f(n-1) +f(n-2))

# n = int(input("enter number"))
# for i in range(n):
#     print(f(i))

    

def f(n):
    if n<=1:
        return n
    elif n==2:
        return 1
    else:
        return (f(n-1)+f(n-2))
n=int(input("enter num."))
z=f(n)
print(z)




# a=[10,20,30,40]
# b=[100,200,300,400] 
# c=[]
# d=[]
# i=0
# while i<len(a): 
#     j=-1
#     while j<len(b)-1: 
#         j=j+1
#     print(a[i],b[j])
#     i=i+1







