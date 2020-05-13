from a_star import Maze, a_star


# Essa será a matriz do labirinto que utilizaremos no exemplo
# Legenda:
# 0: Parede
# 1: Caminho
field = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
]

# Define o ponto inicial e destino
start_point = (2, 0)
end_point   = (0, 7)

# Instancia o Maze
maze = Maze(
    field=field,
    walkable=1,
    start=start_point,
    end=end_point
)

# Chama a função que faz a magia
path = a_star(maze, start_point, end_point)

# Printa o resultado com essa função auxiliar
maze.print_maze_highlighting_nodes(path)
