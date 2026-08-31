class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # using the index-based approach
        stack = []
        mappings = {}

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                mappings[nums2[stack.pop()]] = nums2[i]

            stack.append(i)

        while stack:
            mappings[nums2[stack.pop()]] = -1
        
        return [mappings[num] for num in nums1]