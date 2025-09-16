Numbers = [2,4,1,3,12,7,5,42]

length = len(Numbers)

sorted = False #We assume that the array is initally not sorted

while not sorted: #looping through
    sorted = True #We are going to check whether the array is sorted or not. So we first say Array is sorted, then we check
    for i in range(0,length-1):
        if Numbers[i] > Numbers[i+1]: #If the array is not sorted
            Numbers[i],Numbers[i+1] = Numbers[i+1], Numbers[i]
            sorted = False #since the array was not sorted we assign sorted = False

#To make it modular. You can do the following

def Bubble_sort(MyArray):
    length = len(MyArray)
    sorted = False
    while not sorted:
    sorted = True 
    for i in range(0,length-1):
        if Numbers[i] > Numbers[i+1]: 
            Numbers[i],Numbers[i+1] = Numbers[i+1], Numbers[i]
            sorted = False 
    return MyArray
    