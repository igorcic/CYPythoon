import doctest

opc = 1

while(opc != 0):
    opc = int(input("Digite 1 para adicionar valor ao dicionario ou 0 para sair"))
    if(opc == 1):
        nome = input("Digite o nome da chave: ")
        valor = input("Digite o Valor da chave")
        dicteste = {}
        dicteste[nome] = valor
        print(dicteste)
    else:
        break
