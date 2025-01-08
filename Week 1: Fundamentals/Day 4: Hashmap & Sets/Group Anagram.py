"""
   Assuming strs = ["eat","tea","tan","ate","nat","bat"]
   Since we our result will be nested list i.e. lists in list and the values we need are lists
   Using a dictionary that can carry those lists will be more efficient
   and I'll be using the defaultdict() function and will pass list in it.
   Then we iterate through ever element in strs, sort the word, the sorted word will serve as the key for each list that has a similar
   contains the same elements in the word
   The add them to the dictionary.
"""
from collections import defaultdict


def groupAnagram(strs):
    grp_anagram = defaultdict(list)
    for word in strs:
        sorted_word = "".join(sorted(word))
        grp_anagram[sorted_word].append(word)
    return list(grp_anagram.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagram(strs))
