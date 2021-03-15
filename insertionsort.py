a=[3,2,4,5,9,1]
n=len(a)
for i in range(1,n):
    tmp=a[i]
    j=i
    while (j>0 and tmp<a[j-1]):
        a[j]=a[j-1]
        j=j-1
    a[j]=tmp
print(a)
