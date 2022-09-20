# ID 70655086
from typing import List, Any


def quick_sort(array: List[Any]) -> List[Any]:
    def sort_step(start: int, end: int) -> None:
        if start >= end:
            return

        middle = array[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while array[left] < middle:
                left += 1
            while array[right] > middle:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        sort_step(start, right)
        sort_step(left, end)

    sort_step(0, len(array) - 1)
    return array


if __name__ == '__main__':
    print(
        *[name for _, _, name in quick_sort([
            (lambda name, tasks, fines:
             (-int(tasks), int(fines), name)
             )(
                *input().split()
            ) for _ in range(int(input()))
        ])],
        sep="\n"
    )
