class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        last1 = nums[0]
        last2 = nums[1]
        arr1 = [last1]
        arr2 = [last2]

        for i in range(2, len(nums)):
            val = nums[i]
            if last1 > last2:
                arr1.append(val)
                last1 = val
            else:
                arr2.append(val)
                last2 = val

        arr1.extend(arr2)
        return arr1




# class Solution:
#     def resultArray(self, nums: list[int]) -> list[int]:
#         arr1 = [nums[0]]
#         arr2 = [nums[1]]

#         for i in range(2, len(nums)):
#             if arr1[-1] > arr2[-1]:
#                 arr1.append(nums[i])
#             else:
#                 arr2.append(nums[i])

#         return arr1 + arr2