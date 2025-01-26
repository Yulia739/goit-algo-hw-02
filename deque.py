from collections import deque

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Convert string to lowercase and remove spaces
    s = s.replace(" ", "").lower()
    
    # Create a two-way queue
    char_deque = deque(s)
    
    # Compare characters from both ends of the queue
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


if __name__ == "__main__":
    test_string = input("Enter the string to check for palindrome: ")
    if is_palindrome(test_string):
        print(f"The string '{test_string}' is a palindrome.")
    else:
        print(f"The string '{test_string}' is not a palindrome.")
