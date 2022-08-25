import Funcionario as Func
import time
import linecache

#FUNCOES-----------------------------------------------------
def imprime_funcionarios(funcionarios):
    '''Recebe lista de objeto funcionario e imprime'''
    for i in funcionarios:
        print(i.cod, "|", i.nome, "|", i.cpf, "|", i.data_nascimento, "|", i.salario)

#letra a).2
def gerar_base_de_dados(nome_arq):
    '''Recebe o nome do arquivo e gera uma base de dados de 100 funcionarios. Retorna um objeto funcionario'''
    obj_func = Func.Funcionario()
    for i in range(100):
        obj_func.gera_funcionario(nome_arq)
    print("Base de dados gerada com sucesso")
    return obj_func

#letra b)
def busca_sequencial(nome_arq, cod):
    '''Recebe o nome do arquivo (ordando ou nao) e o codigo do funcionario. Faz a busca por ele e retorna seus dados'''
    with open(nome_arq) as arq:
        start_time = time.time() #Para obter tempo de execucao
        comparacoes = 0
        cod = cod[2:]

        for i in range(101):
            registro = linecache.getline(nome_arq, i)
            registro = registro.split("|")
            if registro[0] == cod:
                print("Tempo de Execucao: %.10f" % (time.time() - start_time), "\nTotal de comparacoes: ", comparacoes) #Obtem o tempo de execucao e imprime
                linecache.clearcache()
                return registro
            else:
                comparacoes = comparacoes + 1

#letra c)
def ordena_arquivo(nome_arq, aux_codF, funcionariosF):
    '''Recebe um arquivo NAO ORDENADO, uma lista de codigos e uma lista de funcionarios'''
    with open(nome_arq, "rb+") as arq:
        start_time = time.time() #Para obter o tempo de execucao

        #Ordenando codigos
        codigos=[bin(int(ele)) for ele in aux_codF]
        codigos=[int(ele,0) for ele in codigos]
        codigos.sort()

        #Apaga todos os dados do arquivo para escreve-los ja ordenados
        arq.seek(0)
        arq.truncate()

        #Escreve arquivo ordenado
        j = 0
        i = 0
        while(i < 100 and  j < 100):
            if int(funcionariosF[i].cod) == codigos[j]:
                arq.write(str(funcionariosF[i].cod).encode())
                arq.write("|".encode())
                arq.write(str(funcionariosF[i].nome).encode())
                arq.write("|".encode())
                arq.write(str(funcionariosF[i].cpf).encode())
                arq.write("|".encode())
                arq.write(str(funcionariosF[i].data_nascimento).encode())
                arq.write("|".encode())
                arq.write(str(funcionariosF[i].salario).encode())
                arq.write("|".encode())
                if j < 99:
                    arq.write("\n".encode())
                j = j + 1
                i = 0
                continue
            i = i + 1
    print("Arquivo ordenado com sucesso!!")
    print("Tempo de Ordernacao: %.10f" % (time.time() - start_time)) #Obtem o tempo de execucao e imprime

#letra d)
def busca_binaria_G(nome_arq, cod: bin, tam):
    '''Recebe um arquivo ORDENADO (pela chave cod), o codigo (em binario) a ser buscado e o tamanho do arquivo em linhas (padrao 100). 
    Retorna os dados do funcionario em formato de LISTA, ou caso nao o encontre retorna falso'''
    left = 0
    right = tam
    while(left <= right):
        middle = int((left+right)//2)
        func = linecache.getline(nome_arq, middle)
        func = func.split("|")
        if int(cod[2:]) == int(func[0]):
            linecache.clearcache()
            return func
        elif int(func[0]) < int(cod[2:]):
            left = middle + 1
        else:
            right = middle - 1
    linecache.clearcache()
    return False

#letra d)
def busca_binaria_L(nome_arq, cod, tam):
    '''Recebe um arquivo ORDENADO (pela chave cod), o codigo a ser buscado e o tamanho do arquivo em linhas (padrao 100). 
    Retorna os dados do funcionario em formato de string, ou caso nao o encontre retorna falso'''
    left = 0
    right = tam+1
    pos_act = tam//2
    linha = linecache.getline(nome_arq, pos_act) 
    cod_act = int(linha.split('|')[0], base = 2)
    while (left < (right-1)):
        if cod < cod_act:
            right = pos_act
        elif cod > cod_act:
            left = pos_act
        pos_act = (right+left)//2
        linha = linecache.getline(nome_arq, pos_act) 
        cod_act = int(linha.split('|')[0], base = 2)
        if cod_act == cod:
            linecache.clearcache()
            return linha
    linecache.clearcache()
    return False
#------------------------------------------------------------

print("---------------------------------------------------------------------------------")
print("GERANDO BASE DE DADOS...")
obj = gerar_base_de_dados("data.dat")

funcionarios = [] #armazena os funcionarios
aux_cod = []

arq = open("data.dat", "rb+") #ABRE ARQUIVO

#Gera uma lista de funcionarios baseada no arquivo
for i in arq.readlines():
    func = Func.Funcionario()
    i = str(i)
    aux = i.split("|")
    func.cod = aux[0][2:]
    aux_cod.append(aux[0][2:])
    func.nome = aux[1]
    func.salario = aux[4]
    func.cpf = aux[2]
    func.data_nascimento = aux[3]
    funcionarios.append(func)

print("---------------------------------------------------------------------------------")
print("BUSCA SEQUENCIAL (ARQUIVO NAO ORDENADO):")
print(busca_sequencial("data.dat", bin(1)))
print("---------------------------------------------------------------------------------")
print("ORDENANDO ARQUIVO (KEYSORT)...")
ordena_arquivo("data.dat", aux_cod, funcionarios)
print("---------------------------------------------------------------------------------")
print("BUSCA BINARIA")
print(busca_binaria_G("data.dat", bin(99), 100))
print("---------------------------------------------------------------------------------")

arq.close() #FECHA ARQUIVO
#print(obj.busca_sequencial(funcionarios, bin(36)).nome)