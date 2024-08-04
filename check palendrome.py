def pelndrome(s):
    s = s.lower()
    return s == s[::-1]
print(pelndrome("Hello"))
print(pelndrome("madam"))
