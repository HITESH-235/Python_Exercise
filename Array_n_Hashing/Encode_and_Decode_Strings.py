# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings. Please implement encode and decode
# LEETCODE Link: https://leetcode.com/problems/encode-and-decode-strings/description/

def encode(str_list):
    # Encodes a list of strings to a single string.
    # Each string is prefixed with its length and a delimiter '%'.
    encoded_str = ""

    for word in str_list:
        encoded_str += str(len(word))+ "%" + word
    return encoded_str


def decode(encoded_str):
    # Decodes the encoded string back into the original list of strings.
    # Uses the delimiter '%' to extract string lengths and substrings.
    decoded_lst = []
    i = 0
    while i < len(encoded_str):
        start = i # always initialize start for new segment

        while encoded_str[i] != "%": # Find delimiter '%' to extract length of word ahead
            i += 1

        word_len = int(encoded_str[start:i])
        start = i + 1 # Move 'start' to start of word
        i = (i+1) + word_len # Move 'i' just ahead of end of word (for next segment)

        word = encoded_str[start:i]
        decoded_lst.append(word)
    return decoded_lst


# Example Usage:
lst = ["%This%","%is%","%a%","%Sentence%"]
encoded_str = encode(lst)
print("Encoded form of list:",encoded_str)
print("Decoded again:",decode(encoded_str)) 


# Another Method: (though unreliable due to use of Non-ASCII character)
# Delimiter = "\x00" # non ASCII character
# def encode_2(str_list):
#     return Delimiter.join(str_list)
# def decode_2(encoded_str):
#     return encoded_str.split(Delimiter)

# __________________________________________________________________________________________________________________________

# Procedure Explained:

#A. ENCODING:
# 1.Create one function for encoding list, takes input of given list and has encoded string as output

# 2.Make 1 single string for storing all words of list in format: (length_of_word ; delimiter(%) ; word)



#B. DECODING:
# 1.Create another function for decoding, takes (input of encoded_string), (returns decoded_list)

# 2.Create a new list of decoded words
#   Run a simple loop(while) to iterate through letters of encoded string

# 3.keep two pointers, one is i(iterable) and start(initiated with i)
#   create another loop with i to find till delimiter (i is now at delimiter%)
#   we can get the integer storing "length of word" going from (start to i-1) (since i is at %)

# 4.now we have to start iterating through the word so put start = i+1 (start of word after %)
#   and then put i equal to i(%)+"length of word"(found earlier), so we have the string from (start to i)
#   store this range (which is the word) in decoded list

#5. repeat this until end
# return decoded list

#*(keep in mind that range in python only goes till n-1, because below text doesn't consider this)

# __________________________________________________________________________________________________________________________