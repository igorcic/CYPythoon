#funções: def

# --------------------- funções ------------------------------
def menu_inicial():
    print("Programa conversão de Temperatura")
    print("<1> converter de celsius para Fahrenheit")
    print("<2> Converter de Fahrenheit para Celsius")

def cel_fahr(temperatura):
    f = temperatura * (9/5) + 32
    return f

def farh_cel(temperatura):
    c = (temperatura - 32) * (5 / 9)
    return c


# ------------------- Main ----------------------
menu_inicial()
escolha = int(input("Escolha o tipo de conversão desejada: "))
if escolha == 1:
    temp = float(input("Digite o valor da temperatura"))
    resposta = cel_fahr(temp)
    print(f"O valor em celsius é {resposta}°F")
if escolha == 2:
    temp = float(input("Digite o valor da temperatura"))
    resposta = farh_cel(temp)
    print(f"O valor em Fahrenheit é {resposta:.3f}°C")
    