"""
  Assuming s = ["h", "e", "l", "l", "o"]
  We will create two pointers that will iterate through the list
  left and right pointer, the left will start from the left with counter +=1
  and the right will start from the right with counter -=1
"""


def reverseString(s):
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s


s = ["h", "e", "l", "l", "o"]
print(reverseString(s))

