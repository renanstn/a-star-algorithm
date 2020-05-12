class Maze:
    """
    Classe que representa o labirinto que será aplicado o algoritmo
    """
    def __init__(self, field, walkable, start, end):
        """
        :field: Matriz que representa o labirinto
        :walkable: Caractere que representa um caminho 'caminhável' no maze
        :start: Ponto de início
        :end: Ponto de destino
        """
        self.field = field
        self.walkable = walkable
        self.start = start
        self.end = end

        self.width = len(self.field[0])
        self.length = len(self.field)

    def check_valid_position(self, position):
        """
        Verifica se uma posição (x,y) informada está dentro dos limites
        do labirinto
        """
        if position[0] < 0 or position[0] > self.width - 1:
            return False
        if position[1] < 0 or position[1] > self.length - 1:
            return False
        return True

    def check_walkable_position(self, position):
        """
        Verifica se uma posição (x,y) informada é 'caminhável' dentro
        do labirinto
        """
        return self.field[position[1]][position[0]] == self.walkable

    def print_maze_highlighting_nodes(self, nodes):
        """
        Printa o field, destacando as posições que receber na lista
        Ideal para debuggar
        """
        positions = [i.position for i in nodes]

        for y in range(self.length):
            for x in range(self.width):
                if (x, y) in positions:
                    print(' * ', end='')
                else:
                    print(' # ', end='')
            print()


class Node:
    """
    Classe que representa um node, um ponto no labirinto.
    Todo node deve ter os atributos F, G e H
    F: Custo total do node (F = G + H)
    G: Distância entre o node e o ponto de partida
    H: Distância entre o node e o ponto de destino
    """
    def __init__(self, maze, parent=None, position=None):
        assert isinstance(maze, Maze)
        self.parent = parent
        self.position = position
        self.maze = maze
        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        """
        Este método é o responsável por comparações entre objetos
        do mesmo tipo. Ele é chamado quando você faz, por exemplo:
        node_a == node_b
        """
        return self.position == other.position

    def get_childrens(self, look_diagonal=False):
        """
        Retorna um array de vizinhos de um node.
        Os vizinhos podem ser tanto os nodes a direita, esquerda, cima, baixo,
        como os 8 nodes adjacentes a ele (considerando os diagonais)
        ? ? ?
        ? N ?
        ? ? ?
        """
        childrens = []

        positions_to_look = [
            # Direita e esquerda
            (1, 0),
            (-1, 0),
            # Acima e abaixo
            (0, 1),
            (0, -1),
        ]

        if look_diagonal:
            diagonal = [
                # Diagonais acima
                (1, 1),
                (-1, 1),
                # Diagonais abaixo
                (1, -1),
                (-1, -1),
            ]
            positions_to_look += diagonal

        for position_to_look in positions_to_look:
            node_position = (
                self.position[0] + position_to_look[0],
                self.position[1] + position_to_look[1]
            )

            if not self.maze.check_valid_position(node_position):
                continue

            if not self.maze.check_walkable_position(node_position):
                continue

            new_node = Node(maze, self, node_position)
            childrens.append(new_node)

        return childrens


def a_star(maze, start, end):
    # Criar node de origem e destino
    start_node = Node(maze, None, start)
    start_node.g, start_node.h, start_node.f = 0, 0, 0
    end_node = Node(maze, None, end)
    end_node.g, end_node.h, end_node.f = 0, 0, 0

    # Inicializar as listas
    open_list = []
    closed_list = []

    # Adicionar o node inicial
    open_list.append(start_node)

    while len(open_list) > 0:
        # Adiciona current node
        current_node = open_list.pop(0)
        closed_list.append(current_node)

        # Verifica se chegou ao destino
        if current_node == end_node:
            print('Node destino alcançado!')
            return

        # Adiciona como children os nodes adjacentes
        childrens = current_node.get_childrens()

        for child in childrens:
            # Verifica se esta children já não foi verificada
            if child in closed_list:
                continue

            # Calcula os valores de F, G, e H para cada vizinho
            child.g = ''
            child.h = ''
            child.f = ''

        # maze.print_maze_highlighting_nodes(childrens)


# -------------------------------------------------------------------
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
# Legenda:
# 0: Wall
# 1: Path

start_point = (2, 0)
end_point   = (0, 7)

maze = Maze(
    field=field,
    walkable=1,
    start=start_point,
    end=end_point
)

a_star(maze, start_point, end_point)
