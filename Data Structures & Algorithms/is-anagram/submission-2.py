class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_hash = {}
        t_hash = {}

        for i in range(len(s)):
            # use get method to fetch the key.
                # if key does not exist automatically add it with a default value of 0 and add 1
                # if key exist just add 1
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1
        

        for key in s_hash:
            if s_hash[key] != t_hash.get(key):
                return False
        
        return True
