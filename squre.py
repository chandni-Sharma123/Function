a=[1,2,3,4,5,6,7,8,9,10]
def s():
    i=0
    sum=0
    while i<len(a):
        b=a[i]*a[i]
        sum=sum+b
        i=i+1
    print(sum)
s()