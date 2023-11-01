# Rachel Whitaker
def count_vowels(string):
    vowels = 'aeiou'
    count = {vowel: 0 for vowel in vowels}
    for char in string:
        if char in vowels:
            count[char] += 1
    return count
