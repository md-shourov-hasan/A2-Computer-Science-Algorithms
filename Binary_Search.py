#In Binary Search, we narrow our search with each iteration, by comparing the values
#The array MUST BE SORTED, we will know why soon
from operator import length_hint

Numbers = [1,4,8,10,23,40,52,61,70] #This is the sorted array


DataToFind = int(input("Enter the number to search: ")) #This is the data we need to search for in the array

def BinarySearch(MyArr, Search): # we are passing the array and the search value as parameter
    start = 0 #we start searching from the first index
    end = len(MyArr) - 1 #till the last index

    while start <= end: #we want to search for the value till start <= end, or else the number is not there
        mid = (start + end)//2 #we look at the middle index, therefore we take the quotient part and ignore the decimal
        if MyArr[mid] == Search:
            return mid
        elif MyArr[mid] > Search: #since MID value is greater than the Search value, we narrow our search, by searching from start to our new end
            end = mid - 1 #as it's useless to search in a bigger range, as the array is already sorted, we know that the search value is not there
        else:
            start = start + 1 #the same ideology is applied here as well
    return -1 #we are returning -1, as we couldn't find the value.

Index = BinarySearch(Numbers, DataToFind)

if Index != -1:
    print(f"The number {DataToFind} is found in index {Index}")
else:
    print("The number is not found")


