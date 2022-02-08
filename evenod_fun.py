# def eveodd():
#     a=[1,2,3,4,5]
#     i=0
#     while i<len(a):
#           if a[i]%2==0:
#             return(a[i],"eee")
#           else:
#             print(a[i],"odd")
#           i=i+1
# eveodd()








def eveodd(a):
  
   i=0
   c=[]
   d=[]
   while i<len(a):
    
    if a[i]%2==0:
        c.append(a[i])
    else:
        d.append(a[i])
    i=i+ 1 
   return(c) 
b=eveodd([12,2,3,4,5,6]) 
print(b)       
      







# def eveodd():
#    a=[12,2,3,4,5,6]
#    i=0
#    while i<len(a):
#        if a[i]%2==0:
#            print(a[i],"ee")
#        else:
#           print(a[i],"odd")
#        i = i + 1
# eveodd()







# a=[10,20,30,[50,60,10]]
# i=0
# l=[]
# while i<len(a):
# 	if type(a[i])==type([]):
# 		j=0
# 		while j<len(a[i]):
# 			l.append(a[i][j])
# 			j+=1
# 	else:
# 		l.append(a[i])
# 	i+=1
# print(l)







# def greet(name, msg):
#     print("Hello", name + ', ' + msg)

# greet("Monica", "Good morning!")