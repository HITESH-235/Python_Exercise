# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings. Please implement encode and decode
# LEETCODE Link: https://leetcode.com/problems/encode-and-decode-strings/description/

def encode(str_list):
    # Encodes a list of strings to a single string.
    # Each string is prefixed with its length and a delimiter '@'.
    encoded_str = ""

    for word in str_list:
        encoded_str += str(len(word))+ "@" + word
    return encoded_str


def decode(encoded_str):
    # Decodes the encoded string back into the original list of strings.
    # Uses the delimiter '@' to extract string lengths and substrings.
    decoded_lst = []
    i = 0
    while i < len(encoded_str):
        start = i

        while encoded_str[i] != "@": # Find delimiter '@' to extract length of word ahead
            i += 1

        word_len = (encoded_str[start:i])
        start = i + 1 # Move past 'start' to start of word
        i = start + int(word_len) # Move past 'i' just ahead of end of word (for next segment)

        word = encoded_str[start:i]
        decoded_lst.append(word)
        start = i # Move 'start' for the next segment as well
    return decoded_lst


# Example Usage:
lst = ["Anjali","hates","Hitesh"]
encoded_str = encode(lst)
print("Encoded form of list:",encoded_str)
print("Decoded again:",decode(encoded_str))