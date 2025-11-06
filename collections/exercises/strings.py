# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.
length_of_string = len(text)
print(length_of_string)
new_text = text[0:12]
print(new_text)

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!

reverse_text = text[-12:]
print(reverse_text)

# 3. Print a slice of the middle 12 characters from 'text'.


print(text[12:24])

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
print('Looping:')
for words in word:
    print('\t'+ words)

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
print('Reverse Looping:')
for words in word[::-1]:   
    print(words,end='\n')

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'.
#  (If you want to be fancy, print 'tomato | otamot').


print("Concate:")
print(word+ "|" +word[::-1])