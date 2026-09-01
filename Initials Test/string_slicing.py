"""String indexing involves naming the position of characters in a string"""
string = "Hassaan"

"""From the above string the indexing can be given as
H = 0, a = 1, s = 2, s = 3, a = 4, a = 4, n = 5,

------------NEGATIVE INDEXING-------------
n = -1, a = -2, a = -3, s = -4, s = -5, a = -6, H = -7 
"""

# String Slicing

print(string[2:5]) # Starts from 2nd index and ends at 5th index(The word on 5th index is not included)

print(string[:3]) # Starts from begining and ends at given number

print(string[3:]) # Starts from 3 and goes to the very end

print(string[-1:-5]) # Starts from last and goes to the 5th word but does not include that word

print(string[0:7:2]) # The last number shows the jump. It means starts from begining and goes to end but include every 2nd word

# REVERSING A STRING 

print(string[::-1]) 


"""Performing different operations on string """
long_string = "Hello World. Nice to be here."
print(long_string.upper()) # Turns every letter into upercase
print(long_string.lower()) # Turns every letter into lowercase
print(long_string.title()) # Turns every first letter into captial
print(long_string.capitalize()) # Make the first word uppercase and rest of them lower case
print(long_string.swapcase()) # Turns lowercase into uppercase and upercase into lower

message = "I love java, java"
print(message.replace("java", "python")) #Replaces the word 
print(message.replace("java", "python", 1))
print(message.find("l")) # if letter isn't present returns -1
print(message.index("j")) # same as find(), but returns error when letter isn't present
print(message.count("a")) # counts the occurance of letters
print(message.startswith("I")) 
print(message.endswith("a"))

# in and not in
print("love" in message) #checks if word is present in string or not and return bool
print("love" not in message)

new_string = "   Hello  Duniya   "

print(new_string.strip()) # This function removes whitespaces from a strip. Similarly, rsplit() remove whitespaces from right and lsplit() removes whitespaces from left.

print(new_string.split())

word = ["Python", "is", "Easy"]
print(" ".join(word))
print(' and '.join(word))

#----------VALIDATION METHODS--------------
age = "1234"
print(age.isdigit()) # Validated if string contains digits

name = "Hassaan"
print(name.isalpha()) # Validates if string contains alphabets

alphanumeric = "Hassaan1234"
print(alphanumeric.isalnum()) # Validates if string has alphabets and numbers


"""Ask the user to enter specific data and validate it"""

country_code = str(input("Enter country code: ").upper())
year = int(input("Enter year: "))
city_code = str(input("Enter city code: ").upper())
package_number = int(input("Enter package number: "))

tracking_code = "-".join([country_code,str(year),city_code,str(package_number)])
print(f"Tracking Code: {tracking_code}")
print(f"Reversed: {tracking_code[::-1]}")
