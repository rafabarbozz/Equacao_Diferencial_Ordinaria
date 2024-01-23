from euler import euler_PVI_simples, euler_PVI_composto

print("-" * 55)
print("-" * 10, " MÉTODO DE EULER PARA 1 EQUAÇÃO ",  "-" * 10)    
print("-" * 55)

equacao = 'x - (2 * y) + 1'
limite_inferior = 0
limite_superior = 1
qtd_passos = 4
y0 = 1

resultado_x, resultado_y = euler_PVI_simples(equacao, limite_inferior, limite_superior, qtd_passos, y0)

for i in range(qtd_passos + 1):
    print(f"Passo {i}:")
    print(f"x[{i}] = {resultado_x[i]} / y[{i}] = {resultado_y[i]}\n")
    

print("-" * 55)
print("-" * 10, " MÉTODO DE EULER PARA 2 EQUAÇÕES ",  "-" * 10)    
print("-" * 55)

equacao_1 = 'y2'
equacao_2 = '2 * x - 3 * y2 + y1'
limite_inferior = 1
limite_superior = 2
qtd_passos = 4
y_10 = 0
y_20 = 1

resultado_x, resultado_y1, resultado_y2 = euler_PVI_composto(equacao_1, equacao_2, limite_inferior, limite_superior, qtd_passos, y_10, y_20)

for i in range(qtd_passos + 1):
    print(f"Passo {i}:")
    print(f"x[{i}] = {resultado_x[i]} / y[1][{i+1}] = {resultado_y1[i]} / y[2][{i}] = {resultado_y2[i]}\n")
    