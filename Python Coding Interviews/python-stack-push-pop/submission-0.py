from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    reversed_list = []
    for _ in range(len(arr)):
        removed_el = arr.pop()
        reversed_list.append(removed_el)
    
    return reversed_list


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
