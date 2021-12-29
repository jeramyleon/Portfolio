print("National\n\"Basketball\"\nAssociation")
# Prints the string with new lines(\n), added quotes within print statement(\"), and actual "\" characters.

phrase = "National Basketball Association" # This is how you assing a variable

print(phrase) # Prints the variable named phrase
print(phrase + " is cool") # Prints phrase plus extra string bit using plus sign

print(phrase.lower()) # Prints lowercase version of phrase
print(phrase.upper()) # Prints uppercase version of phrase
print(phrase.isupper()) # Returns True or False if phrase is uppercase
print(phrase.upper().isupper()) # Applies uppercase and then checks if it is uppercase which is True

print(len(phrase)) # Prints length of phrase
 
print(phrase[0]) # Accesses first element. Index indices always start at 0. 
print(phrase[3]) # Accesses fourth element.
print(phrase.index("N")) # Prints which index N is at
print(phrase.index("n")) # Prints which index n is at
print(phrase.index("National")) # Prints starting index of "National" 
# print(phrase.index("1")) # Prints which index "1" is at and returns an error if not found, in this case it returns an error, uncomment to see the error message
print(phrase.replace("National", "Lebron")) # Replaces "National" with "Lebron" in phrase.
