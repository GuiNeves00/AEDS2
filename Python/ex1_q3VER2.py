arq = open("notas.txt", "a+")
media = 0.0

matematica = float(input("Digite a nota em matematica "))
media += matematica
arq.write(str(matematica) + '\n')

fisica = float(input("Digite a nota em fisica "))
media += fisica
arq.write(str(fisica) + '\n')

quimica = float(input("Digite a note em quimica "))
media += quimica
arq.write(str(quimica) + '\n')

media = media / 3

arq.write("\n" + str(media))

arq.close()