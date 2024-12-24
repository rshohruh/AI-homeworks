text = input("Enter a string: ").lower()
vowels = "aeiou"
num_vowels = sum(1 for char in text if char in vowels)
num_consonants = sum(1 for char in text if char.isalpha() and char not in vowels)
print(f"Vowels: {num_vowels}, Consonants: {num_consonants}")
