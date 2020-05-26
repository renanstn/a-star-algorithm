# A* (A Star) Algorithm

>Implementação de um algoritmo A* (A star) em Python.

Este algoritmo recebe:
- um labirinto, feito a partir de uma matriz 2D
- uma posição de partida
- uma posição de destino
- o caractere pelo qual ele pode "caminhar"

E calcula a menor rota para chegar até o destino.

## Como funciona

Imaginando o labirinto como uma matriz bidimensional, o algoritmo tenta sempre avançar na direção do destino, usando valores de "custos" para cada node.

O **custo** de um node é dado pela fórmula:

`F = G + H`

Onde:
- G = Distância entre o **node atual** e o **node de partida**
- H = Distância entre o **node atual** e o **node de destino**

Para melhor entendimento do algoritmo A*, leia [este](https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2) artigo, que serviu de base para eu desenvolver este estudo.

![exemplo de A* funcionando](https://github.com/Doc-McCoy/a-star-algorithm/blob/master/images/animation.gif)

## Rodando

Este projeto possui um arquivo de exemplo em `src/`, onde os seguintes passos são dados:

- Primeiramente definimos nosso "labirinto", no meu caso, fiz uma matriz 2D com numeros 1 e 0:

```
[0, 1, 1, 1, 1]
[1, 1, 1, 1, 0]
[1, 0, 0, 1, 1]
[1, 0, 0, 0, 1]
[0, 1, 1, 1, 1]
[0, 1, 0, 1, 0]
[0, 1, 0, 1, 1]
[1, 1, 0, 0, 1]
```

>Considere o caractere 0 como parede, e o 1 como caminhos

*Neste labirinto, só se pode caminhar para cima, baixo, direita e esquerda. Não vamos trabalhar com as diagonais neste exemplo (mas o código está preparado para tratar as diagonais também, se você optar)*

- Defina o ponto de entrada, e de saída do labirinto

```py
start_point = (4, 0)
end_point   = (0, 7)
```

- Inicialize um objeto `Maze`, passando como parâmetro a matriz, o caractere que representa onde ele pode percorrer, o ponto de entrada, e o ponto de saída

```py
maze = Maze(
    field=field,
    walkable=1,
    start=start_point,
    end=end_point
)
```

- Agora, basta chamar a função `a_star` passando o maze para ela resolver. Aqui também informamos se ele deve considerar movimentos na diagonal ou não

```py
path = a_star(maze, move_in_diagonals=False)
```

- O que será retornado em `path`, será a lista de coordenadas de todo o caminho desde o início até o fim do labirinto

- Utilizei a função auxiliar `print_maze_highlighting_nodes` para exibir o caminho que o algoritmo descobriu, no caso o caminho é desenhado usando `*`:

```
#  #  #  *  *
#  #  #  *  #
#  #  #  *  *
#  #  #  #  *
#  *  *  *  *
#  *  #  #  #
#  *  #  #  #
*  *  #  #  #
```

## Créditos

O GIF que ilustra o algoritmo funcionando veio [deste](https://atsushisakai.github.io/PythonRobotics/) repositório (que é maravilhoso, diga-se de passagem).

E o artigo que me baseei para fazer este estudo foi [este](https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2), porém fiz várias modificações para melhorar alguns pontos.
