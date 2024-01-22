# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

#Count how many times the substring "Emma" appeared
str_x = "Emma is good developer. Emma is a writer"
print("Given String: ", str_x)

#Print the number of occurrences
count_substring = str_x.count("Emma")
print(f"Emma appeared {count_substring} times")