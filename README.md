# A* (A Star) Algorithm

*Implementação de um algoritmo A* (A star) em Python.*

Este algoritmo recebe um labirinto 2D, um **ponto de partida**, **um ponto de destino**, **onde ele pode "caminhar"**, e calcula a menor rota para chegar até o destino.

Imaginando o labirinto como uma matriz bidimensional, o algoritmo tenta sempre avançar na direção do destino, usando valores de "custos" para cada node.

O **custo** de um node é dado pela fórmula:

`F = G + H`

Onde:
- G = Distância entre o **node atual** e o **node de partida**
- H = Distância entre o **node atual** e o **node de destino**

![exemplo de A* funcionando](https://github.com/Doc-McCoy/a-star-algorithm/blob/master/images/animation.gif)

### Créditos

Este GIF maravilhoso e auto-explicativo é veio [deste](https://atsushisakai.github.io/PythonRobotics/) incrível repositório.

E o artigo que me baseei para fazer este algoritmo foi [este](https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2), porém fiz várias modificações para melhorar alguns pontos.
