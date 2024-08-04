def count_vowel(s):
    vowel = "aeiouAEIOU"
    return sum(1 for char in s if char in vowel)
print(count_vowel("Hello World"))