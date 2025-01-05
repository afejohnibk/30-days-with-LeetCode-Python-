"""
THis takes up more memory although its a simple alternative

def validAnagram(s, t):
    return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"

print(validAnagram(s, t))

Another alternative which does not take up much memory
is using the counter in the python library

from collective import counter
def validAnagram(s, t):
    return counter(s) == counter(t)
"""


def validAnagram(s, t):
    counter_s = {}
    counter_t = {}
    for char in s:
        counter_s[char] = counter_s.get(char, 0) + 1
    for char in t:
        counter_t[char] = counter_t.get(char, 0) + 1
    return counter_s == counter_t


s = "anagram"
t = "nagaram"

print(validAnagram(s, t))
