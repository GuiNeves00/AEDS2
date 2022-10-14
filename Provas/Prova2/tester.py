#ESTE PROGRAMA APENAS TESTA SE CADA PARTICAO INDIVIDUAL ESTA ORDENADA!
#Para isto, os arquivos "particao0.dat", "particao1.dat", ..., "particaoN.dat", antes precisam existir/serem criados atraves das funcoes de selecao
#decidi deixa-lo na entrega pois pode ser util para vc durante a correcao.

qt_arquivos = 9
nomeArq = [f'particao{i}.dat' for i in range(0,qt_arquivos)]

ant = -1
qt = 0
media = 0
for i in nomeArq:
    with open(i, "rb") as arq:
        ordenado = True
        for i in arq.readlines():
            
            index =int( i.split('|'.encode())[0], base=2)
            media += len(i)
            qt+=1
            print(index)
            if index > ant:
                ant = index
            else:
                ordenado = not ordenado
                print("nao ordenado")
                break
        
        if ordenado:
            print("ORDENADO")
    ant = -1
print("Media ", media/qt)
