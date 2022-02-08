# x = "global "

# def foo():
#     global x
#     y = "local"
#     x = x * 2
#     print(x)
#     print(y)

# foo()






# x = 5

# def foo():
#     x = 10
#     print("local x:", x)


# foo()
# print("global x:", x)








def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()





# c = 0 # global variable

# def add():
#     global c
#     c = c + 2 # increment by 2
#     print("Inside add():", c)

# add()
# print("In main:", c)





# def foo():
#     x = 20

#     def bar():
#         global x
#         x = 25
    
#     print("Before calling bar: ", x)
#     print("Calling bar now")
#     bar()
#     print("After calling bar: ", x)

# foo()
# print("x in main: ", x)









# def absolute_value(num):
#     """This function returns the absolute
#     value of the entered number"""

#     if num >= 0:
#         return num
#     else:
#         return -num


# print(absolute_value(2))

# print(absolute_value(-4))