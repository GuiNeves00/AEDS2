arq = open("notas.txt", "a+")

matematica = int(input("Digite a nota em matematica"))
fisica = int(input("Digite a nota em fisica"))
quimica = int(input("Digite a note em quimica"))

notas = []
notas.append(matematica)
notas.append(fisica)
notas.append(quimica)

arq.writelines(str(notas))

arq.seek(0, 0)
media = 0
for linha in notas:
    media += linha

media = media / 3

arq.write("\n"+str(media))

arq.close()