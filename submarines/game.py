import random
from submarines.board import in_bounds, count_remaining_ships,render_public


def init_game(size: int, n_ships: int, max_shots: int, *, rng: random.Random | None =None) -> dict:
    return {
            "size": size,
            "ships": [],
            "shots": [],
            "n_ships": n_ships,
            "max_shots": max_shots,
            "shots_used": 0
            }
    
def shoot(state: dict, x: int, y: int) -> tuple[bool, str]:
    if in_bounds(state["size"], x, y):
        rend_pub = render_public(state["ships"],state["shots"])
        if rend_pub[x][y] == "O":
            state["shots_used"] +=1
            state["max_shots"] -= state["shots_used"]
            return (True, "great shoot!")
        
    
def is_won(state: dict) -> bool:
    return count_remaining_ships(state["ships"], state["shots"]) == 0
        
def is_lost(state: dict) -> bool:
    if state["shots_used"] >= state["max_shots"] and not is_won(state):
        return True
    return False

def shots_left(state: dict) -> int:
    return state["max_shots"] - state["shots_used"]

def remaining_ships(state: dict) -> int:
    count = 0
    for i in range(state["ships"]):
        for j in range(i):
            if state["ships"][i][j] == 1:
                count += 1
    return count

    
    
