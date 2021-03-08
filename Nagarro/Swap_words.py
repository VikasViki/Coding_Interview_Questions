## Question : wrtie a method to swap the places of the given two words in the specified string
## Test Case 1 : Vikas means Perfect, Vikas , Perfect
## Output : Perfect means Vikas

def swap_words(string, word1, word2):
    #Converting the given string into a list of words using the split() function of python i.e based on spaces
    string = string.split()
    
    #Creating two indices for both the words
    word1_index = -1
    word2_index = -1
    
    #Traversing through the words of the list and checking if the current word is one of the word to be replaced
    for index in range(len(string)):
        
        #If the current word of the string is word1 then update the index of word1_index
        if string[index] == word1:
            word1_index = index
        
        #If the current word of the string is word2 then update the index of word2_index
        elif string[index] == word2:
            word2_index = index
            
            #Since once we have obtained the index of word2 we need not to traverse the list further so we stop iterating the loop
            break
    
    #Swapping the words of the string using there corresponding index
    string[word1_index], string[word2_index] = string[word2_index], string[word1_index]
    
    #Returning the list of words as single string after swaping the words
    return " ".join(string)

#Taking the inputs of the string and words from the user
string = input()
word1 = input()
word2 = input()

#Printing the string after swaping the words
print(swap_words(string, word1, word2))
