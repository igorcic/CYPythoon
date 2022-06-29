#coleções
# variaveis que ppegar mais de uma informação do usuario.

# listas = [] -> Ordenada, Mutavel e permite repetições, indexação
# tuplas = () -> Ordenadas, Permitem repetições, Imutaveis, indexação

# Dicionarios = {"chave": informação} -> Ordenado, Mutavel, Não permite repetição
# set = {} = Não ordenadas, Não indexaveis, nenhum membro pode ser duplicado

listaFrutas = ["maçã", "banana","limão"]
print(listaFrutas[1])

tuplaFrutas = ("maçã", "banada", "limão")
print(tuplaFrutas[0])

dicionarioFrutas = {"maça": "5 reais", "banana": 7, "limão": 8}
print(dicionarioFrutas["maça"])

colecaoAleatria = {"maçã", True, 6, 5.7}
print(colecaoAleatria)

# keys() - Apresenta todas as chaves do dicionario
print(dicionarioFrutas.keys())

#values() - Apresenta todos os valores armazenados
print(dicionarioFrutas.values())

#items() - keys + values
print(dicionarioFrutas.items())