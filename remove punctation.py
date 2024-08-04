import string

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

print(remove_punctuation("Hello, world!")) 
