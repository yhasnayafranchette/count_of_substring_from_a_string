# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

#Show and display the given string
str_x = "Emma is good developer. Emma is a writer"
print("Given String: ", str_x)

#Count and print the number of occurrences
count_substring = str_x.count("Emma")
print(f"Emma appeared {count_substring} times")