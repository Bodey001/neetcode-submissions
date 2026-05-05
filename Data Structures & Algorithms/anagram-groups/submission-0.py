class Solution:
    # Anagrams --> the frequency of the each character in a string is important
    # Form an alphabets array of size 26 representing 0 for each of the alphabets
        # For each word in the inputted list, increase the index respective to the alphabets array.
            # For example, eat --> 
                # e is the 5th letter on the alphabets but index 4 gets increased by one
                # a is the first, index zero gets increased by one
            
        # Store the string in a hash table using the increased alphabets list as the key and the inputted word as the value

        # Note using ASCII:
            # a = 97 --> 97 - 97 = index 0

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_table = {}
        
        for string in strs:
            alphabets = [0] * 26        # Initialize the array for the alphabets

            for char in string:
                index = ord(char) - ord('a')        # Generate the index of the letter
                alphabets[index] += 1           # Increase the respective elements by 1

            alphabets_string = f"{alphabets}"       # Convert list to string in order to set it as a key in the hast_table

            if alphabets_string in hash_table:
                hash_table[alphabets_string].append(string)
            else:
                hash_table[alphabets_string] = [string]

        return [hash_table[key] for key in hash_table]



        # print(alphabets)