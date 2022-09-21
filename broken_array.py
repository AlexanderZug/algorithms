# ID 70696519
def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        numbers_left = nums[left]
        if numbers_left == target:
            return left
        middle = left + (right - left) // 2
        numbers_middle = nums[middle]
        if (
                numbers_left <= target and (
                target < numbers_middle or numbers_middle < numbers_left
        )
        ) or (
                target < numbers_middle < numbers_left):
            right = middle
        else:
            left = middle + 1
    return -1
