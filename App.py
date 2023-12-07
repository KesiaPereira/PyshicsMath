#Bibliotecas Utilizadas.
import matplotlib.pyplot as plt
import numpy as np
import math

#Configurando o previamente o Plano Cartesiano.
def configurar_plano_cartesiano():
    ax = plt.axes()
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.grid()
    plt.plot([-10, 10], [0, 0], color="gray")
    plt.plot([0, 0], [-10, 10], color="gray")

#Gerar um plano cartesiano vazio.
def gerar_plano_cartesiano():
    configurar_plano_cartesiano()
    plt.quiver(0, 0, 0, 0, angles="xy", scale_units="xy", scale=1, color="red")
    plt.show()
    return "Fim do exemplo."

#Gerar vetores em um plano cartesiano.
def gerador_de_vetores(a, b, c):
    vetores = np.array([a, b, c])
    origens = np.array([[0, 0, 0], [0, 0, 0]])

    ax = plt.axes()
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.grid()

    plt.quiver(*origens, vetores[:, 0], vetores[:, 1], angles='xy', scale_units='xy', scale=1, color = ["r", "g", "b"])
    plt.plot([-10, 10], [0, 0], color="gray")
    plt.plot([0, 0], [-10, 10], color="gray")
    plt.show()
    return "Fim da exibição."

#Funcao para calcular distancia.
def calcular_distancia(ponto1, ponto2):
    dx = ponto1[0] - ponto2[0]
    dy = ponto1[1] - ponto2[1]
    return math.sqrt(dx**2 + dy**2)

#Funcao para calcular o campo da carga.
def calcular_campo_carga(carga, posicao, ponto_p):
    dx = ponto_p[0] - posicao[0]
    dy = ponto_p[1] - posicao[1]
    distancia = calcular_distancia(ponto_p, posicao)

    campo_x = (9 * carga * dx) / distancia**3
    campo_y = (9 * carga * dy) / distancia**3

    return campo_x, campo_y

#Realizando os calculos.
def calcular_campo_eletrico(cargas, posicoes, ponto_p):
    campo_total = [0, 0]

    for carga, posicao in zip(cargas, posicoes):
        campo_carga = calcular_campo_carga(carga, posicao, ponto_p)
        campo_total[0] += campo_carga[0]
        campo_total[1] += campo_carga[1]

    print("O Campo Elétrico no ponto P é igual a:")
    return campo_total


#Introdução
print("Olá! Vamos calcular o Campo Elétrico em um ponto P.\nPrimeiramente, começamos com um Plano Cartesiano Vazio:")
input("Pressione ENTER para continuar.")
print(gerar_plano_cartesiano())

print("Agora, seguiremos com os valores para dar início aos cálculos.\nInforme o valor dos pontos a seguir:")

#Definindo as coordenadas de cada ponto.
x1 = float(input("Insira o valor de x no 1º ponto:\n"))
y1 = float(input("Insira o valor de y no 1º ponto:\n"))
vetor1 = [x1, y1]
x2 = float(input("Insira o valor de x no 2º ponto:\n"))
y2 = float(input("Insira o valor de y no 2º ponto:\n"))
vetor2 = [x2, y2]
x3 = float(input("Insira o valor de x no 3º ponto:\n"))
y3 = float(input("Insira o valor de y no 3º ponto:\n"))
vetor3 = [x3, y3]

#Chamando o plano cartesiano com os vetores.
print(gerador_de_vetores(vetor1, vetor2, vetor3))

print("Precisamos, antes de tudo, definir nossas cargas!\nINFORME O VALOR DAS CARGAS A SEGUIR.")

#Definindo as cargas de cada ponto.
c1 = float(input("Insira o valor da carga 1:\n"))
c2 = float(input("Insira o valor da carga 2:\n"))
c3 = float(input("Insira o valor da carga 3:\n"))

#Definindo o ponto P.
print("Não esqueca de informar o ponto P!\nINFORME OS VALORES A SEGUIR.")
xp = float(input("Insira o valor X do ponto P:\n")) 
yp = float(input("Insira o valor Y do ponto P:\n"))

#Juntando todos os dados.
cs = [float(input(f"Insira o valor da carga {i + 1}:\n")) for i in range(3)]
pontos = [[float(input(f"Insira o valor de x no {i + 1}º ponto:\n")),
           float(input(f"Insira o valor de y no {i + 1}º ponto:\n"))] for i in range(3)]
p = [float(input("Insira o valor X do ponto P:\n")), float(input("Insira o valor Y do ponto P:\n"))]


print(calcular_campo_eletrico(cs, pontos, p))
print("Fim do programa!")