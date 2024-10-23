print("*"*20,"Selection sorting","*"*20)
import time
start=time.time()
def selectionsort(a):
    n=len(a)
    for i in range(n-2):
        min=i
        for j in  range(i+1,n-1):
            if a[j]<a[min]:
                temp=a[j]
                a[j]=a[min]
                a[min]=temp
alist=[34,46,43,27,57,41,45,21,70]
print("Before sorting:",alist)
selectionsort(alist)
print("After sorting:",alist)
end=time.time()
print(f"Runtime of the program is:{end-start}")
print("")
