import random
import matplotlib.pyplot as plt


alturas = []
pesos = []

for _ in range(100):
    altura = random.randint(150, 200)
    if altura < 160:
        peso = random.randint(50, 65)
    elif altura < 180:
        peso = random.randint(60, 80)
    else:
        peso = random.randint(75, 100)

    alturas.append(altura)
    pesos.append(peso)


n = len(alturas)
sum_x = sum(alturas)
sum_y = sum(pesos)

sum_xy = 0
for i in range(n):
    sum_xy += alturas[i] * pesos[i]

sum_x2 = sum(altura ** 2 for altura in alturas)

#calculando m y b
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - m * sum_x) / n


regresion_lineal = [m * altura + b for altura in alturas]


#grafica
plt.scatter(alturas, pesos, label='Datos originales', color='blue')
plt.plot(alturas, regresion_lineal, label=f'Regresión lineal: y={m:.2f}x + {b:.2f}', color='red')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Ajuste de Curva: Regresión Lineal')
plt.legend()
plt.show()
