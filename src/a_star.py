class Maze:
    """
    Classe que representa o labirinto que será aplicado o algoritmo
    """
    def __init__(self, field, walkable, start, end):
        """
        field: Matriz que representa o labirinto
        walkable: Caractere que representa um node 'caminhável' no labirinto
        start: Ponto de início
        end: Ponto de destino
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
        Ideal para debuggar ou conferir o caminho encontrado
        nodes: Uma lista de nodes ou uma lista de corrdenadas
        """
        if isinstance(nodes, Node):
            positions = [i.position for i in nodes]
        else:
            positions = nodes

        for y in range(self.length):
            for x in range(self.width):
                if (x, y) in positions:
                    print(' * ', end='')
                else:
                    print(' # ', end='')
            print() # Pula linha


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

            new_node = Node(self.maze, self, node_position)
            childrens.append(new_node)

        return childrens


def a_star(maze, move_in_diagonals=False):
    # TODO Dividir essa função em funções menores

    # Criar node de origem e destino
    start_node = Node(maze, None, maze.start)
    start_node.g, start_node.h, start_node.f = 0, 0, 0
    end_node = Node(maze, None, maze.end)
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
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            # Retorna o caminho reverso
            return path[::-1]

        # Adiciona como children os nodes adjacentes
        childrens = current_node.get_childrens(move_in_diagonals)

        for child in childrens:
            # Verifica se esta children já não foi verificada
            if child in closed_list:
                continue

            # Calcula os valores de F, G, e H para cada vizinho
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if child in open_list:
                index = open_list.index(child)
                if child.g > open_list[index].g:
                    continue

            open_list.append(child)
