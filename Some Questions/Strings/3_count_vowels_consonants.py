string = "Basudev Samanta"
vowels = "aeiouAEIOU"


count_vowels = sum(1 for char in string if char in vowels)
count_consonants = sum(1 for char in string if char.isalpha() and char not in vowels)

print(f"Vowels is : {count_vowels}\nConsonants is: {count_consonants}")