text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
space_count = 0
lowercase_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
    if char == " ":
        space_count += 1
    if char.islower():
        lowercase_count += 1

print("Number of Vowels:", vowel_count)
print("Number of Consonants:", consonant_count)
print("Number of Spaces:", space_count)
print("Number of Lowercase Letters:", lowercase_count)