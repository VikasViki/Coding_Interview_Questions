## Question : Create a method to arrange the zero one array in such a way such that all the zero's are at even position
## and all the one's are at the odd position of the array. If the count of zero is greater than one or vice versa add the extra elements 
## at the end of the array.

#Basic Approach
def Arrange_Zero_One(array):
    #Creating two counters of zero and one
    zero_count = 0
    one_count = 0
    
    #Traversing through the array to get the number of zero's and one's in the array
    for element in array:
        if element == 0:
            zero_count += 1
        else:
            one_count += 1
    
    #Initializing the index as zero at the beginning    
    index = 0
    
    #Assigning the corresponding value at the index based on odd and even position
    while (zero_count != 0 and one_count != 0):
        if index%2 == 0 and zero_count != 0:
            array[index] = 0
            index += 1
            zero_count -= 1
        elif index%2 != 0 and one_count != 0:
            array[index] = 1
            index += 1
            one_count -= 1
    
    #If the count of zero's is greater than the count of one's
    while zero_count != 0:
        array[index] = 0
        index += 1
        zero_count -= 1
    
    #If the count of one's is greater than the count of zero's
    while one_count != 0:
        array[index] = 1
        index += 1
        one_count -= 1
    
    #Returning the array after arranging the zero's and one's 
    return array

#Taking the input of array in the form of space separated list
array = list(map(int,input().split()))

#Printing the arranged array
print(Arrange_Zero_One(array))
