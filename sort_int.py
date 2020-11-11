def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for k in range(low,high):
        if arr[k]<=pivot:
            i=i+1;
            arr[i],arr[k]=arr[k],arr[i]
            arr[i+1],arr[high]=arr[high],arr[i+1]
            return(i+1)
def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,pi-1)
        quicksort(arr,pi+1,high)

arr=[10,7,8,9,1,5]
n=len(arr)
quicksort(arr,0,n-1)
print("\nSorted arry:")
for i in range(n):
    print("%d->"%arr[i])
