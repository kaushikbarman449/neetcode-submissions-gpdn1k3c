from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    freqChar = defaultdict(int)
    for ch in s:
        freqChar[ch] += 1
    
    return freqChar


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    # my_dict = {}
    # for sublist in nums:
    #     if sublist[0] in my_dict:
    #         my_dict[sublist[0]].extend(sublist[1:]) 
    #     else:
    #         my_dict[sublist[0]] = sublist[1:]
    # return my_dict

    my_dict = defaultdict(list)
    for sublist in nums:
        my_dict[sublist[0]].extend(sublist[1:])
    
    return my_dict
    

# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
