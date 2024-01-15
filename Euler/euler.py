from calcular_eq import calcular_equação

def euler_PVI(equacao: str, limite_inf: float, limite_sup: float, qtd_passos: int, y0: float):
    
    Vet_x = [None] * qtd_passos
    Vet_y = [None] * qtd_passos    
    Fxy = 0
    
    h = (limite_sup - limite_inf) / qtd_passos
    x = limite_inf
    y = y0
    
    Fxy = calcular_equação(equacao, x, y)

    for i in range(1, qtd_passos + 1):
        y_ant = y
        x_ant = x
        
        x = limite_inf + i * h
        y = y_ant + h * Fxy
        
        print(f"y{i} = {y_ant} + {h} * {2 * y_ant * x_ant}")
        print(f"i: {i}, x: {x}, y: {y}, Fxy: {Fxy}")
        print()
                
        Fxy = calcular_equação(equacao, x, y)
        
        #print(f"i: {i}, x: {x}, y: {y}, Fxy: {Fxy}")
        
        Vet_x[i - 1] = x
        Vet_y[i - 1] = y
    
    return Vet_x, Vet_y