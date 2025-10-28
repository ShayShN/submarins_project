from submarines.board import render_public,count_remaining_ships,render_reveal
from submarines.game import shots_left, is_lost,is_won
from submarines.placement import place_random_ships

def parse_coords(raw: str, *, one_based: bool = True) -> tuple[int, int] | None:
    pass

def print_status(state: dict) -> None:
    print(count_remaining_ships(state["ships"],state["shots"] ))
    print(shots_left(state))
    print(render_public(state["ships"], state["shots"]))
    
def print_end(state: dict, won: bool) -> None:
    if is_won(state):
        print(render_public(state["ships"],state["shots"]))
    if is_lost(state):
        print(render_reveal(state["ships"],state["shots"]))
        