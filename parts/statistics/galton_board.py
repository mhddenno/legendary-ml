from random import randint
import matplotlib.pyplot as plt

LEVELS: int = 10
COLUMNS: int = 11
BALLS: int = 10000


def main() -> None:
    result: dict = {}
    for _ in range(BALLS):
        init_column = (COLUMNS - 1) / 2
        for _ in range(LEVELS):
            if init_column == 0 or init_column == COLUMNS - 1:
                break
            elif randint(0, 1):
                init_column += 1
            else:
                init_column -= 1
        result[init_column] = result.get(init_column, 0) + 1
    plt.bar(result.keys(), result.values())
    plt.xlabel("Column")
    plt.ylabel("Balls")
    plt.title("Distribution of balls in Galton borad")
    plt.show()


if __name__ == "__main__":
    main()
