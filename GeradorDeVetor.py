import matplotlib.pyplot as plt
import numpy as np

vetores = np.array([[2, 4],[6, 8],[10, 12]])
origens = np.array([[0, 0, 0], [0, 0, 0]])

plt.quiver(*origens, vetores[:,0], vetores[:,1], color = "red", scale=1)
plt.show()

#x0 = 0
#y0 = 0
#origem = [x0, y0]
#
#x = float(input("Insira o valor de x: "))
#y = float(input("Insira o valor de y: "))
#vetor = [x, y]
#
#ax = plt.axes()
#ax.set_xlim(([-10, 10]))
#ax.set_ylim(([-10, 10]))
#ax.quiver(origem, x, y, angles="xy", scale_units="xy", scale=1, color="red")
#ax.annotate(f"({vetor[0]}, {vetor[1]})", (vetor[0], vetor[1]), fontsize=10)
#ax.grid()
#
#plt.plot([-10, 10], [0, 0], color="gray")
#plt.plot([0, 0], [-10, 10], color="gray")
#plt.show()
#
#print(input("Pressione Enter para finalizar."))