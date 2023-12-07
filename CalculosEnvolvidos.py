import math

cargas = [2, 10, 3]
posicoes = [(1, 0), (-2, 3), (4, -1)]
ponto_p = (4, -2)

campo_total = [0, 0]

for carga, posicao in zip(cargas, posicoes):
    dx = ponto_p[0] - posicao[0]
    dy = ponto_p[1] - posicao[1]
    distancia = math.sqrt(dx**2 + dy**2)
    campo_x = (9 * carga * dx) / distancia**3
    campo_y = (9 * carga * dy) / distancia**3
    campo_total[0] += campo_x
    campo_total[1] += campo_y

print(campo_total)