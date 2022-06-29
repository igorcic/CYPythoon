nome = "igor "
sobrenome = "bastos"
grito = "OLA MUNDO"
email = "igor@gmail.com"
nomeCompleto = nome + sobrenome

# a função lem retorna a quantidade numerica de strings
x = len(nome)

# As strings são guardadas como vetores, tendo cada letra sua posição
print(nome[1])

print(email.find("@"))
print(nome.find("a"))

# Upper converte para maiusculo
letra = nome[0].upper()
# Subistituição caracteres
print(nome.replace('i',letra))


menusculo = grito.lower()
letra2 = grito[0].upper()
print(menusculo.replace("o",letra2))
