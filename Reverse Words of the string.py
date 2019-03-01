##Question : Reverse each word of the given string
## Testcase 1: Vikas Want To Become Perfect
## Output : sakiV tnaW oT emoceB tcefreP


#Method to reverse the words of the string using the start and end index
def reverse_word(string, start_index, end_index):
    #Swap word at starting index and ending index until starting index becomes greater than the ending index
    while start_index <= end_index:
        string[start_index],string[end_index] = string[end_index],string[start_index]
        start_index += 1
        end_index -= 1

#Taking the input of the string in the form of list
string = list(input())

#Initially the starting index will be 0 and ending index will be -1 
start_index = 0
end_index = -1

#Finding the length of the string using python len() method
string_length = len(string)

for index in range(string_length):
    #If the current character is space,then the word between the spaces will be reversed
    if string[index] == " ":
        #End index is one less than current index because we want to swap the word without affecting the space character
        end_index = index-1
        
        #Function to swap the word of the string
        reverse_word(string,start_index,end_index)
        
        #Start index is updated to end_index + 2 becuase now the start_index will be at the first letter of the next word 
        #As at current index is the space character
        start_index = end_index + 2

#Since the last word of the string doesnot end with space character we have swap it by changing the end_index
#to last letter of the last word
end_index = string_length-1
reverse_word(string,start_index, end_index)

#Printing the string by converting it from list
print("".join(string))
