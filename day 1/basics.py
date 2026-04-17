#datatypes in python

name="R Liana"
age= 21
height=  5.1
isTrainer = False

print("Name:", type(name))
print("Age:", type(age))
print("Height:", type(height))
print("Is Trainer:", type(isTrainer))

#ctrl+shift+~ open terminal
#python basics.py to run the code in terminal

#non primitive datatypes: lists,tuples,sets,dictionaries
languages_known = ["Python","Java","C++","C"]
#list represented using square brackets []
#list is ordered, mutable, we can change the values in list, allows duplicates
print("Languages Known:", type(languages_known))

#tuples represented using parentheses ()
#tuple is ordered, immutable, we cannot change the values in tuple, allows duplicates
even_numbers = (2,4,6,8,10,12)
print("Even Numbers:", type(even_numbers))

#sets represented using curly braces {}
#sets are unordered, mutable, we can change the values in set, does not allow duplicates
odd_numbers = {1, 3, 5, 7, 9}
print("Odd Numbers:", type(odd_numbers))

#dictionaries represented using curly braces {}, key-value pairs
#dictionaries are unordered, mutable, we can change the values in dictionary, does not allow
profile = {"name": "R Liana",
"age": 21,
"college": "City Engineering College",
"role": "Student",
"department": "Artificial Intelligence and Data Science"}
print("Profile:", type(profile))