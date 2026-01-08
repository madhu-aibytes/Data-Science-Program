def palindrome_check(s):
    stack = list(s)        # create stack from string
    reversed_s = ""
    
    while stack:
        reversed_s += stack.pop()   # pop characters to reverse string
    
    return s == reversed_s          # check if original equals reversed

# Main
s = input("Enter a string to check palindrome: ")

if palindrome_check(s):
    print("Palindrome")
else:
    print("Not a palindrome") 