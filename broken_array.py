# ID 70653764
def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        numbers_left = nums[left]
        if numbers_left == target:
            return left
        middle = left + (right - left) // 2
        numbers_middle = nums[middle]
        if numbers_middle == target:
            return middle
        if (
                (numbers_left < target or numbers_left == target) and (
                target < numbers_middle or numbers_middle < numbers_left
        )
        ) or (
                target < numbers_middle < numbers_left):
            right = middle
        else:
            left = middle + 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
