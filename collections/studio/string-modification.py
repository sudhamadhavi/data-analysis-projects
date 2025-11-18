my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.


new_string = my_string[3:] + my_string[:3]

print(new_string)



# Use a template literal to print the original and modified string in a descriptive phrase.

print(f"Original_string : {my_string}")
print(f"MOdified_string : {new_string}")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
user_input = int(input("Enter the number of letters to relocate: "))
new_text = my_string[user_input:] + my_string[:user_input]
print(new_text)
        

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. 
# Also, the template literal should note the error.

user_input = int(input("Enter the number of letters to relocate: "))
if user_input > len(my_string):
    print("Error: Input too long! Defaulting to 3 letters instead.")
    user_input = 3
    new_text = my_string[user_input:] + my_string[:user_input]
print(f"Original string: {my_string}")
print(f"After moving {user_input} letters: {new_text}")