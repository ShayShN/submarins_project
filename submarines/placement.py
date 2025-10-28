import random

def place_random_ships(ships: list[list[int]], n: int) -> None:
    for _ in range(n):
        for i in random.randrange(ships):
            for j in random.randrange(ships):
                ships[i][j] = 1

                