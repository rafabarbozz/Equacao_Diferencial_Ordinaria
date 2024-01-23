def euler_PVI_simples(equacao: str, limite_inf: float, limite_sup: float, qtd_passos: int, y_0: float):
    
    Vet_x = [None] * (qtd_passos + 1)
    Vet_y = [None] * (qtd_passos + 1)
    Fxy = 0
    
    h = (limite_sup - limite_inf) / qtd_passos
    x = limite_inf
    y = y_0
    
    Fxy = eval(equacao)

    Vet_x[0] = x
    Vet_y[0] = y_0
    
    for i in range(1, qtd_passos + 1):
        y_ant = y
        
        x += h 
        
        y = y_ant + h * Fxy # yi = yi-1 + h * f(xi-1, yi-1)
                
        Fxy = eval(equacao)
                
        Vet_x[i] = x
        Vet_y[i] = y
    
    return Vet_x, Vet_y

def euler_PVI_composto(equacao_1: str, equacao_2: str, limite_inf: float, limite_sup: float, qtd_passos: int, y_10: float, y_20: float):
    Vet_x = [None] * (qtd_passos + 1)
    Vet_y1 = [None] * (qtd_passos + 1)
    Vet_y2 = [None] * (qtd_passos + 1)
    Fxy_1 = 0
    Fxy_2 = 0
    
    h = (limite_sup - limite_inf) / qtd_passos
    x = limite_inf
    y1 = y_10
    y2 = y_20
    
    Fxy_1 = eval(equacao_1)
    Fxy_2 = eval(equacao_2)
    
    Vet_x[0] = x
    Vet_y1[0] = y_10
    Vet_y2[0] = y_20
    
    for i in range(1, qtd_passos + 1):
        y1_ant = y1
        y2_ant = y2
        
        x += h
        
        y1 = y1_ant + h * Fxy_1
        y2 = y2_ant + h * Fxy_2
        
        Fxy_1 = eval(equacao_1)
        Fxy_2 = eval(equacao_2)
        
        Vet_x[i] = x
        Vet_y1[i] = y1
        Vet_y2[i] = y2
        
    return Vet_x, Vet_y1, Vet_y2
        
        