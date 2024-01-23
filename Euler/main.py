from euler import euler_PVI_simples, euler_PVI_composto

print("-" * 51)
print(" PROGRAMA PARA CALCULAR EDO's PELO MÉTODO DE EULER ")    
print("-" * 51)

opcao = 0
print("1 - Método de Euler para 1 equação\n"
      "2 - Método de Euler para 2 equações\n")

opcao = int(input("Digite a opção que deseja: "))


if opcao == 1:
    print("-" * 55)
    print("-" * 10, " MÉTODO DE EULER PARA 1 EQUAÇÃO ",  "-" * 10)    
    print("-" * 55)

    equacao = ''
    limite_inferior = 0.0
    limite_superior = 0.0
    qtd_passos = 0
    y0 = 0.0

    equacao = str(input("Digite a equação: "))
    limite_inferior = float(input("Digite o limite inferior: "))
    limite_superior = float(input("Digite o limite suprior: "))
    qtd_passos = int(input("Digite a quantidade de passos: "))
    y0 = float(input("Digite o y0: "))
    
    resultado_x, resultado_y = euler_PVI_simples(equacao, limite_inferior, limite_superior, qtd_passos, y0)
    print()
    for i in range(qtd_passos + 1):
        print(f"Passo {i}:")
        print(f"x[{i}] = {resultado_x[i]} / y[{i}] = {resultado_y[i]}\n")


elif opcao == 2:
    print("-" * 55)
    print("-" * 10, " MÉTODO DE EULER PARA 2 EQUAÇÕES ",  "-" * 10)    
    print("-" * 55)

    equacao_1 = ''
    equacao_2 = ''
    limite_inferior = 0
    limite_superior = 0
    qtd_passos = 0
    y_10 = 0
    y_20 = 0

    equacao_1 = str(input("Digite a equação 1: "))
    equacao_2 = str(input("Digite a equação 2: "))
    limite_inferior = float(input("Digite o limite inferior: "))
    limite_superior = float(input("Digite o limite suprior: "))
    qtd_passos = int(input("Digite a quantidade de passos: "))
    y_10 = float(input("Digite o y10: "))
    y_20 = float(input("Digite o y20: "))

    resultado_x, resultado_y1, resultado_y2 = euler_PVI_composto(equacao_1, equacao_2, limite_inferior, limite_superior, qtd_passos, y_10, y_20)
    print()
    for i in range(qtd_passos + 1):
        print(f"Passo {i}:")
        print(f"x[{i}] = {resultado_x[i]} / y[1][{i+1}] = {resultado_y1[i]} / y[2][{i}] = {resultado_y2[i]}\n")