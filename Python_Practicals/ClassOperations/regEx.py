import re

nameAge = '''Walter is 50 and aii Jesse is 25
Gus is 47 and Mike aiaii is 60. aiiii 
+911122336655
+915566332211
+918426546281
75549-6546
79552-9568
85652-9695'''



# pattern = re.compile(r'\d{5}-\d{4}') # Will find number   
pattern = re.compile(r'\+91\d{10}') # Will find number   
matches = pattern.finditer(nameAge)

for match in matches:
    print(match)



# #-----------------------

# Meta Characters
# [] A set of characters
# \ Signals a special sequence (can also be used to escape special characters)
# . Any character (except newline character)
# ^ Starts with
# $ Ends with
# * Zero or more occurrences
# + One or more occurrences
# {} Exactly the specified number of occurrences
# | Either or
# () Capture and group
# Special Sequences
# \A Returns a match if the specified characters are at the beginning of the string
# \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

# \d Returns a match where the string contains digits (numbers from 0-9)
# \D Returns a match where the string DOES NOT contain digits
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character
# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \W Returns a match where the string DOES NOT contain any word characters
# \Z Returns a match if the specified characters are at the end of the string


# pattern = re.compile(r'a') # Normal Search
# pattern = re.compile(r'.us') # . Any Character
# pattern = re.compile(r'^Walter') # ^ Starts with Character
# pattern = re.compile(r'60$') # $ Ends with Character
# pattern = re.compile(r'ai*') # * Zero or more Occurences
# pattern = re.compile(r'ai+') # + One or more Occurences
# pattern = re.compile(r'ai{2}') # {n} Exactly Specified number or more Occurences
# pattern = re.compile(r'(ai){2}') # () makes a group
# pattern = re.compile(r'ai{2}|Jesse') # | Either or

# pattern = re.compile(r'\AWalter') # \A Returns a match if specified characters are at the begining of the string

# pattern = re.compile(r'r\b') # \b Returns a match if specified characters are at the begining or at the end of a word