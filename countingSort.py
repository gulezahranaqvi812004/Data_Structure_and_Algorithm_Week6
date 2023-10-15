import random
def countingSort(array):
    maximum=max(array)
    minimum=min(array)
    outputArray=[0]*len(array)
    counting=[0]*(maximum-minimum+1)

    for j in array:
        k=j-minimum
        counting[k]+=1

    for l in range(1,len(counting)):
     counting[l]+=counting[l-1]
 
    for i in range(len(array)-1,-1,-1):
        j=array[i]-minimum
        counting[j]-=1
        outputArray[counting[j]]=array[i]

    return outputArray

array=[]
for i in range(0,10):
    j=random.randint(2,10)
    array.append(j)
print(array)
sortedArray=countingSort(array)
print(sortedArray)
