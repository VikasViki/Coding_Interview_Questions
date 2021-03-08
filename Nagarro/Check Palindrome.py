# Question : Create a program to check whether the given string can be converted into a palindrome or not.
# Test Case 1 : hello 
# Output : false (we can't arrange the letters of the above string in any way to form a palindrome)
# Test Case 2 : tests
# Output : true (tests can be converted to 'tsest' or 'stets' and so on)

## Note : Always create your program with less time and space complexities


def checkPalindrome(string):
    #It will create a dictionary of each distinct letters of the string with frequency as 0 initially
    #If you print the below line it will display something like this
    #{'h': 0, 'o': 0, 'e': 0, 'l': 0}
    characters_frequency = dict.fromkeys(list(string),0)
    
    #Traversing through each character of the string and increasing there corresponding frequency in the characters_frequency dictionary
    for character in string:
        characters_frequency[character] += 1
        
    #Creating an odd counter to check how many characters of the string is of odd length
    odd_count = 0
    
    #Traversing through each item of the dictionary in the pair of character and frequency
    for character,frequency in characters_frequency.items():
        #Incrementing the odd_count if the current character has a odd frequency
        if frequency%2 != 0:
            odd_count += 1
        #If there are two characters in the string of odd length then it can't be a palindrome
        if odd_count == 2:
            break
    
    #Returning the result based on the number of odd characters
    if odd_count == 2:
        return False
    else:
        return True
       

#Taking the string input
string = input()
print(checkPalindrome(string))
    
