def add_underscores(txt):
    vowels = "aeiou"
    result = []
    for i, char in enumerate(txt):
        result.append(char)
        if (i + 1) % 3 == 0 or char in vowels:
            result.append('_')
    return ''.join(result).rstrip('_')

print(add_underscores("hello"))  
print(add_underscores("assalom"))  
print(add_underscores("abcabcdabcdeabcdefabcdefg"))  
