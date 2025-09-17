#In insertion sort, we take the 2nd index element and then compare it with 
#the previous value, then we keep on swapping the larger number
#to not lose the key element we are comparing with, we store it in 
#a variable called "key". Dry run for further understanding



Data = [2,3,1,13,8,12,0,4]

length = len(Data)

for i in range(1,length):
    key = Data[i]
    previous = i - 1
    while previous >= 0 and Data[previous] > key:
        Data[previous + 1] = Data[previous]
        previous -= 1
    Data[previous + 1] = key

#For modular sorting

def insertionSort(Arr):
    length = len(Arr)
    for i in range(1,length):
        key = Arr[i]
        prev = i - 1
        while prev >= 0 and Arr[prev]>key:
            Arr[prev + 1] = Arr[prev]
            prev -= 1
        Arr[prev + 1] = key
    




