proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]
print(strings)

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.

for s in strings:
    print(f"\nAnalyzing: '{s}'")

    if "," in s:
        print("→ Words are separated by commas.")
    elif ";" in s:
        print("→ Words are separated by semicolons.")
    elif " " in s:
        print("→ Words are separated by spaces.")
    else:
        print("→ No recognizable separator found.")
# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.

for s in strings:
    print(f"\nOriginal string: {s}")

    # Check if string uses commas
    if "," in s:
        # Split into list, reverse it, and join again
        parts = s.split(",")
        parts.reverse()  # or parts = parts[::-1]
        new_string = ",".join(parts)
        print(f"→ Reversed comma-separated string: {new_string}")
    else:
        print("→ Not comma-separated; no changes made.")

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
 
    for s in strings:
     print(f"\nOriginal string: {s}")
    if ";" in s:
        # Split into list, reverse it, and join again
        parts = s.split(",")
        parts.reverse()  # or parts = parts[::-1]
        new_string = ",".join(parts)
        print(f"→ Reversed comma-separated string: {new_string}")
    else:
        print("→ Not comma-separated; no changes made.")


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

    for s in strings:
     print(f"\nOriginal string: {s}")
    if " " in s:
        # Split into list, reverse it, and join again
        parts = s.split(",")
        parts.reverse()  # or parts = parts[::-1]
        new_string = ",".join(parts)
        print(f"→ Reversed comma-separated string: {new_string}")
    else:
        print("→ Not comma-separated; no changes made.")

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
    for s in strings:
     print(f"\nOriginal string: {s}")
    if ",  " in s:
        # Split into list, reverse it, and join again
        parts = s.split(",")
        parts.reverse()  # or parts = parts[::-1]
        new_string = ",".join(parts)
        print(f"→ Reversed comma-separated string: {new_string}")
    else:
        print("→ Not comma-separated; no changes made.")