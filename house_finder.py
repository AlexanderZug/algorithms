# id 69865000

from typing import List


def house_finder(length: int, houses: List[str]) -> List[int]:
    result = [0] * length
    nulls = [index for index, house in enumerate(houses) if house == '0']
    first_null = nulls[0]
    for house_index in range(0, first_null):
        result[house_index] = first_null - house_index
    for previous_house, current_house in zip(nulls, nulls[1:]):
        for house_index in range(previous_house + 1, current_house):
            result[house_index] = min(
                house_index - previous_house, current_house - house_index
            )
    last_null = nulls[-1]
    for house_index in range(last_null + 1, length):
        result[house_index] = house_index - last_null
    return result


#
if __name__ == '__main__':
    print(*house_finder(int(input()), input().split()))
