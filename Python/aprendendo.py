arquivo = open("texto.txt", "w")

frases = list()
frases.append("TreinaWeb \n")
frases.append("Python \n")
frases.append("Arquivos \n")
frases.append("Django \n")

arquivo.writelines(frases)

arquivo = open("texto.txt", "r")
linhas = arquivo.read()
print(linhas)

arquivo.close()