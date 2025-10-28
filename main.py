from submarines.board import ask_size,create_matrix,create_bool_matrix, render_reveal
from submarines.game import render_public

def play(size: int = 6, n_ships: int = 6, max_shots: int = 10, *, one_based: bool = True) ->None:
    pass


ask_user_size = ask_size()
create_regular = create_matrix(ask_user_size)
create_bool = create_bool_matrix(ask_user_size)
rend_pub = render_public(state["ships"], state["shots"])
