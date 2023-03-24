#LC-383
#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        counts = dict()
        for s in ransomNote:
            counts[s] = counts.get(s, 0) + 1
        for s in magazine:
            if s in counts.keys():
                counts[s] -= 1

        for val in counts.values():
            if val > 0 :
                return False
        return True