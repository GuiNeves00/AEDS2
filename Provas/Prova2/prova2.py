#CONJUNTO DE FUNCOES (questoes 1, 2 e 3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

import Funcionario as Func

M = 6 #quantidade de registros a serem passados para a memoria principal

def gerar_base_de_dados(nome_arq):
    '''Recebe o nome do arquivo e gera uma base de dados de 100 funcionarios. Retorna um objeto funcionario'''
    obj_func = Func.Funcionario()
    for i in range(100):
        obj_func.gera_funcionario(nome_arq)
    print("Base de dados gerada com sucesso!")
    return obj_func


def retorna_pos_menor(lista):
    '''Funcao auxiliar para retornar a posicao do menor elemento de uma lista'''
    min = 999
    pos = 0
    for i in range(len(lista)):
        if int(lista[i].cod, base=2) < min:
            min = int(lista[i].cod, base=2)
            pos = i
    #print(f"RETORNO MENOR: {int(lista[pos].cod, base=2)}")
    return pos

#QUESTAO 1
def selecao_com_substituicao(nomeArqEntrada):
    '''Realiza a selecao com substituicao, dado o nome do arquivo de entrada'''
    with open(nomeArqEntrada, "rb") as arquivo:
        fimDeArquivo = False
        particao = 0
        registros = []
        congelados = []

        # "1 - ler M registros do arquivo para a memoria"
        for i in range(M):
            linha = arquivo.readline()
            if not linha:
                fimDeArquivo = True
                break
            registro = Func.Funcionario()
            registro.le_Linha(linha)
            registros.append(registro)

        
        while not fimDeArquivo or len(registros) != 0: # "6 - Caso existam em memoria registros nao congelados, voltar ao passo 2"
            
            # "2 - Selecionar, no array em memoria, o registro r com menor chave"
            while len(registros) > 0:
                menor = registros.pop(retorna_pos_menor(registros))
                menor.grava_funcionario(f"particao{particao}.dat") # "3 - Gravar o registro r na particao de saida"

                # "4 - Substituir no array em memoria, o registro r pelo proximo registro do arquivo de entrada"
                aux = arquivo.readline() #pega o proximo registro do arquivo
                if aux: 
                    aux2 = Func.Funcionario()
                    aux2.le_Linha(aux) 
                    #se o indice do registro recuperado é menor que o ultimo registro gravado
                    #congelo o registro recuperado 
                    # "5 - Caso a chave deste ultimo seja menor do que a chave recem gravada, considera-lo congelado e ignora-lo no restante do processamento"
                    if int(aux2.cod, base=2) < int(menor.cod,base=2):
                        congelados.append(aux2)
                    else:
                        registros.append(aux2)
                else:
                    fimDeArquivo = True
                    continue
                
            # "7 - Caso contrario: 1.fechar a particao de saida|2.descongelar os registros congelados|3.abrir nova particao de saida|4.voltar ao passo 2"
            particao += 1
            i = len(congelados)
            for j in range(i):
                registros.append(congelados.pop())


#QUESTAO 2                
def selecao_natural(nomeArqEntrada):
    '''Realiza a selecao natural, dado o nome do arquivo de entrada'''
    # "1 - Ler M registros do arquivo para a memória"
    with open(nomeArqEntrada, "rb") as arquivo:
        fimDeArquivo = False
        particao = 0
        registros = []
        congelados = 0
        for i in range(M): #recupera M registros para a memória principal
            linha = arquivo.readline()
            if not linha:
                fimDeArquivo = True
                break
            registro = Func.Funcionario()
            registro.le_Linha(linha)
            registros.append(registro)
        
        #" 2- Selecionar, no array em memoria, o registro r com menor chave"
        while not fimDeArquivo or len(registros) != 0:
            while congelados < M: # "6 - Caso ainda exista espaco livre no reservatorio, voltar ao passo 2"
                #print(len(registros))
                if len(registros) == 0:
                    break
                menor = registros.pop(retorna_pos_menor(registros))
                menor.grava_funcionario(f"particao{particao}.dat") # "3 - Gravar o registro r, na particao de saida"
                
                #" 4 - Substituir, no array em memoria, o registro r pelo proximo registro do arquivo de entrada"
                aux = arquivo.readline()
                if aux: 
                    aux2 = Func.Funcionario()
                    aux2.le_Linha(aux)
                    # "5 - Case a chave deste ultimo seja menor do que a chave recem gravada, grava-lo no reservatorio e subsitituir, no array em memoria, o registro r pelo proximo registro do arquivo de entrada"
                    #se o indice do registro recuperado é menor que o ultimo registro gravado
                    #congelo o registro recuperado
                    if int(aux2.cod, base=2) < int(menor.cod, base=2):
                        aux2.grava_funcionario("reservatorio.dat")
                        congelados += 1
                    else:
                        registros.append(aux2)
                else:
                    fimDeArquivo = True
                    continue
            
            # "7 - Caso contrario: 1.fechar a particao de saida|2.copear os registros do reservatorio para o array em memoria|3.esvaziar o reservatorio|4.abrir nova particao de saida|5.voltar ao passo 2"
            particao += 1
            reservatorio = open("reservatorio.dat", "rb+")
            #recupera os registros dos congelados
            for i in range(congelados):
                linha = reservatorio.readline()
                registro = Func.Funcionario()
                registro.le_Linha(linha)
                registros.append(registro)

            congelados = 0
            reservatorio.close()
            reservatorio = open("reservatorio.dat", "wb")
            reservatorio.write("".encode())
            reservatorio.close()

def todos_acabados(lista):
    '''Verifica se todas as posicoes do vetor sao iguais a -1'''
    for i in lista:
        if i != -1:
            return False 
    return True    

def le_linha_arquivo(arquivo, linha):
    '''Le a linha de um dado arquivo'''
    for line_number, line in enumerate(arquivo):
        if line_number == linha:
            arquivo.seek(0,0)
            return str(line)
    return -1

#QUESTAO 3
def intercalacao(nomeArquivoSaida, numeroDeParticoes):
    '''Realiza a intercalacao, dado o nome do arquivo de entrada e o numero de particoes geradas pelos metodos de selecao natural e/ou selecao com substituicao'''
    posicoes = [0 for x in range(numeroDeParticoes)]
    arquivos = []

    #Abre os arquivos e salva em uma lista a referencia a eles
    for i in range(numeroDeParticoes):
        arquivos.append(open(f"particao{i}.dat", "rb"))
    menor = 9999999
    posMenor = [0,0]

    #Verifica o topo de cada particao, buscando o menor. ("A cada iteracao do algoritmo, o topo da pilha com menor chave e gravado no arquivo de saida e eh substituido pelo seu sucessor")
    while not todos_acabados(posicoes):
        for i in range(numeroDeParticoes):
            if posicoes[i] == -1:
                continue
            linha = le_linha_arquivo(arquivos[i], posicoes[i])
            #print(linha)
            if linha == -1:
                posicoes[i] = -1
                continue
            aux = linha.split("|")
            #print(f"arq: {i} pos: {posicoes[i]}")
            if int(aux[0][2:], base=2) < menor:
                menor = int(aux[0][2:], base=2)
                posMenor = [i, posicoes[i]]
                
        menor = 99999
        linha = le_linha_arquivo(arquivos[posMenor[0]], posMenor[1])
        if posicoes[posMenor[0]] != -1:
            posicoes[posMenor[0]] += 1
        print(posicoes[0], posicoes[1])
        if linha != -1:
            print(f"Gravando linha, {posMenor[0]}, {posMenor[1]}: ", linha)
            aux = Func.Funcionario()
            aux.le_Linha(linha)
            aux.grava_funcionario(nomeArquivoSaida)

#MENU----------------------------------------------------------------------------------------------------------------------------------------------------------------
menu = 0
while(menu != 1):
    menu = int(input("----------MENU----------\n1 - Gerar base de dados\n"))
    if menu == 1:
        gerar_base_de_dados("data.dat")
    else:
        menu = int(input("Opcao invalida. Tente novamente\n1 - Gerar base de dados\n"))

while(True):
    menu = int(input("----------MENU----------\n2 - Selecao com substituicao\n3 - Selecao natural\n"))
    if menu == 2:
        selecao_com_substituicao("data.dat")
        print("Selecao com substituicao realizada com sucesso!")
        break
    elif menu == 3:
        selecao_natural("data.dat")
        print("Selecao natural realizada com sucesso!")
        break
    else:
        print("Opcao invalida. Tente novamente")
    
while(menu != 4):   
    menu = int(input("----------MENU----------\n4 - Intercalacao\n"))
    if menu == 4:
        intercalacao("SAIDA.dat", 9) #9 = numero de particoes
        print("Intercalacao realizada com sucesso!")
    else:
        print("Opcao invalida. Tente novamente")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

print("FIM DO PROGRAMA!")