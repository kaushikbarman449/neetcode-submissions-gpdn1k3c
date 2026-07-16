from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for index, num in enumerate(nums):
        if num == 7:
            return index
    
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    first_seven = None
    for i in range(len(nums)):
        if nums[i] == 7:
            first_seven = i
            break
    
    for i in range(first_seven + 1, len(nums)):
        if nums[i] == 7:
            return i - first_seven



# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
