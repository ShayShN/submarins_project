
from submarines.placement import place_random_ships


def ask_size():
    while True:
        user_input = input("enter a size of matrix: ")
        if user_input.isdigit() and user_input:
            return int(user_input)
        continue
 
def create_matrix(size: int=5, fill: int = 0) -> list[list[int]]:
    matrix = []
    for row in range(size):
        arr = []
        for col in range(size):
            arr.append(fill)  
        matrix.append(arr)
    return matrix 



def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    matrix_bol = []
    for i in range(size):
        arr_bol = []
        for j in range(size):
            arr_bol.append(fill)
        matrix_bol.append(arr_bol)
    return matrix_bol 
#    
def in_bounds(size: int, x: int, y: int) -> bool:
    return  x <= size >= y 

def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    count =0
    for i in range(ships):
        for j in range(i):
            if ships[i][j] == 1 and shots[i][j] == False:
                count +=1
    return count

def render_public(ships: list[list[int]], shots: list[list[bool]]) -> str:
    matrix_str = []
    for i in range(ships):
        arr = []
        for j in range(i):
            if ships[i][j] == 1 and shots[i][j] == True:
                arr[i][j].append("V")
            if ships[i][j] == 0 and shots[i][j] == True:
                arr[i][j].append("X")
            if shots[i][j] == False:
                arr[i][j].append("O")
        matrix_str.append(arr)
    return matrix_str

def render_reveal(ships: list[list[int]], shots: list[list[bool]]) -> str:
    place_random_ships(ships, 3)
    for i in range(ships):
         for j in range(i):
             if ships[i][j] == 1:
                 shots[i][j] = True
    return ships
             

                        