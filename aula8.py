# leitura, escrita - substituir conteudos, escrita - inserir novos dados

arquivo = open("texto.txt","a")
frases = list()
frases.append("Igor \n")
frases.append("rafael \n")
frases.append("joão \n")
frases.append("victor \n")
arquivo.writelines(frases)


