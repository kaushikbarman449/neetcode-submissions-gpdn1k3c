from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    freq = {}
    for ch in word:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
