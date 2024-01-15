from calcular_eq import calcular_equação
from euler import euler_PVI

# Métedo de Euler para uma equação

equacao = 'x - (2 * y) + 1'
limite_inferior = 0
limite_superior = 1
qtd_passos = 10
y0 = 1

resultado_x, resultado_y = euler_PVI(equacao, limite_inferior, limite_superior, qtd_passos, y0)

print(f"Passo 0:")
print(f"x[0] =  {limite_inferior} / y[0] = {y0}\n")
for i in range(qtd_passos):
    print(f"Passo {i+1}:")
    print(f"x[{i+1}] = {resultado_x[i]} / y[{i+1}] = {resultado_y[i]}\n")