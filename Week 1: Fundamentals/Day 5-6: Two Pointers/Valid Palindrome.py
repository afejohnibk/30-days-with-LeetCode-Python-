def validPalindrome(s):
    newstr = ""
    for char in s:
        if char.isalnum():
            newstr += char.lower()
    return newstr == newstr[::-1]


s = "A man, a plan, a canal: Panama"
print(validPalindrome(s))

