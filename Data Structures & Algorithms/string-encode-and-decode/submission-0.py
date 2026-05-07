class Solution:
    # We can use an encoding approach where we start with a number representing the length of the string, 
    # followed by a separator character (let's use # for simplicity), and then the string itself. 
    # To decode, we read the number until we reach a #, then use that number to read the specified number of characters as the string.

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        
        # print(encoded_string)
        return encoded_string            


    # Using Two Pointers
        # One Pointer at the beginning of the element to operate on 
        # The other pointer at the end of the element group to operate on
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
            
            # Pick the number
            length_str = s[i:j]
            length = int(length_str)

            # Use the string after the "#" as the beginning of the string
            # and the number to select the end on the string
            string_start = j + 1
            string_end = string_start + length

            string = s[string_start:string_end]

            # Append the parse string to the list
            decoded_string.append(string)

            # Set the new position of i to the end of the string
            i = string_end

        return decoded_string
