#To initialise an empty 2D array, we initialise it as normal array

numbers = []

#The way we are going to append data will decide the dimension of the array

for i in range(10):
    numbers.append([0, -1])
    #just filling in the array

print(numbers[9][1])
