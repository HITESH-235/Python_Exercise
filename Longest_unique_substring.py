# Given a string s, find the length of the longest substring without duplicate characters. A substring is a contiguous sequence of characters within a string.
# LEETCODE link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def longest_unique_substring(s):
    window = set()                  # Stores characters in the current window (no duplicates)
    max_length = 0                  # Tracks the maximum length found
    start = 0                       # Left pointer of the sliding window
    end = 0                         # Right pointer of the sliding window

    while end < len(s):
        # If current character is already in the set, shrink window from the left
        while s[end] in window:
            window.remove(s[start])
            start += 1

        # Add the new character to the set
        window.add(s[end])

        # Update max_length if this window is longer
        current_window_length = end - start + 1
        max_length = max(max_length, current_window_length)

        # Move the right pointer forward
        end += 1

    return max_length

# Example usage
s = "pwwkew"
print(longest_unique_substring(s))  # Output: 3
