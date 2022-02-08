def primeorNot(num):
    if num > 1:
      for i in range(2,num):
        if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
        else:
           print(num,"is a prime number")

    else:
        print(num,"is not a prime number")
primeorNot(406)







# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)





# def multiply(a,b):
#      multiply=a*b
#      return multiply
# print(multiply(3,4))





# def Avg(number1,number2,number3):
#     sum=number1+number2+number3/3
#     print(sum)
# Avg(1,3,2)



# def voter(age):
#     if age < 18:
#        print("eligible")
#     else:
#        print("not eligible")
# voter(20)




def distance(kms):
    if kms < 20:
       print("close")
    elif kms < 50:
       print("median")
    else:
       print("far")
distance(30)