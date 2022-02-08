def num():
   Num = int(input("Please Enter any Number :- "))
   i = 1
   Sum = 0
   while(i < Num):
       if(Num % i == 0):
           Sum = Sum + i
       i = i + 1
   if (Sum == Num):
       print("It is a Perfect Number",i)
   else:
       print("It is not a Perfect Number",i)
num()




