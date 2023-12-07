#Bibliotecas Utilizadas.
import matplotlib.pyplot as plt
import numpy as np
import math

#Gerar um plano cartesiano vazio.
def gerar_plano_cartesiano():
    x = 0
    y = 0

    ax = plt.axes()
    ax.set_xlim([-10, 10]) #Limite X do plano cartesiano.
    ax.set_ylim([-10, 10]) #Limite Y do plano cartesiano.
    ax.quiver(0, 0, x, y, angles="xy", scale_units="xy", scale=1, color="red")
    ax.grid()

    plt.plot([-10, 10], [0, 0], color="gray")
    plt.plot([0, 0], [-10, 10], color="gray")
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

#Realizando os calculos.
def calcular_campo_eletrico(cargas, posicoes, ponto_p):
    campo_total = [0, 0]  # Inicializa o campo elétrico total como zero

    for carga, posicao in zip(cargas, posicoes):
        dx = ponto_p[0] - posicao[0]
        dy = ponto_p[1] - posicao[1]
        distancia = math.sqrt(dx**2 + dy**2)

        campo_x = (9 * carga * dx) / distancia**3
        campo_y = (9 * carga * dy) / distancia**3

        campo_total[0] += campo_x
        campo_total[1] += campo_y

    print("O Campo Elétrico no ponto P é igual a:")
    return campo_total


#Introdução
input("Olá! Para inciarmos nossos cálculos, vamos utilizar de um plano cartesiano.\nPRESSIONE ENTER PARA PROSSEGUIR COM O EXEMPLO.")
print(gerar_plano_cartesiano())

print("Agora, seguiremos com os valores para dar início aos cálculos.\nINFORME O VALOR DOS PONTOS A SEGUIR.")

#Definindo as coordenadas de cada ponto.
x1 = float(input("Insira o valor de x no 1º ponto:\n"))
y1 = float(input("Insira o valor de y no 1º ponto:\n"))
vetor1 = [x1, y1]
x2 = float(input("Insira o valor de x no 2º ponto::\n"))
y2 = float(input("Insira o valor de y no 2º ponto::\n"))
vetor2 = [x2, y2]
x3 = float(input("Insira o valor de x no 3º ponto::\n"))
y3 = float(input("Insira o valor de y no 3º ponto::\n"))
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
cs = [c1, c2, c3]
pontos = [vetor1, vetor2, vetor3]
p = [xp, yp]

print(calcular_campo_eletrico(cs, pontos, p))
print("Fim do programa!")