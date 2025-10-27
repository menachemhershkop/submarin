def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    return [[0 for _ in range(size)] for _ in range(size)]
def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
   return [[0 for _ in range(size)] for _ in range(size)]
def in_bounds(size: int, x: int, y: int) -> bool:
    if x > size or y > size:
        return False
    return True
def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    shot_count=0
    for i,j in enumearte(ships):
        for x,y in emumerate(j):
            if shots[x][y]==ships[i][j]:
                shot_count+=1
    return shot_count
def render_public(ships: list[list[int]], shots: list[list[bool]]) -> str:
    pass
def render_reveal(ships: list[list[int]], shots: list[list[bool]]) -> str:
    pass



