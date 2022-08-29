# id 69840804

from typing import List


def house_finder(houses: List[str]) -> List[int]:
    result = [0] * len(houses)
    nulls = [index for index, house in enumerate(houses) if house == '0']
    first_null = nulls[0]
    for i in range(0, first_null):
        result[i] = first_null - i
    for i, j in zip(nulls, nulls[1:]):
        for k in range(i + 1, j):
            result[k] = min(k - i, j - k)
    last_null = nulls[-1]
    for i in range(last_null + 1, len(houses)):
        result[i] = i - last_null
    return result


if __name__ == '__main__':
    input()
    print(*house_finder(input().split()))

# id 69840416

NUMBER_OF_PLAYERS = 2
SYMBOLS = '123456789'


def scores_calculation(keys: int, template: str) -> int:
    return sum(
        0 < template.count(symbol) <= keys * NUMBER_OF_PLAYERS
        for symbol in SYMBOLS
    )


if __name__ == "__main__":
    print(
        scores_calculation(
            keys=int(input()),
            template='{}{}{}{}'.format(input(), input(), input(), input()),
        )
    )
