# id 69887744
from collections import Counter

NUMBER_OF_PLAYERS = 2
SYMBOLS = '123456789'


def scores_calculation(keys: int, template: str) -> int:
    return sum(
        True
        for symbol, amount in Counter(template).items()
        if symbol in SYMBOLS and amount <= keys
    )


if __name__ == "__main__":
    print(
        scores_calculation(
            keys=int(input()) * NUMBER_OF_PLAYERS,
            template=f'{input()}{input()}{input()}{input()}',
        )
    )
