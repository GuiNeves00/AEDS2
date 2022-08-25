import Funcionario as Func
import time
import linecache

#FUNCOES-----------------------------------------------------
def imprime_funcionarios(funcionarios):
    '''Recebe lista de objeto funcionario e imprime'''
    for i in funcionarios:
        print(i.cod, "|", i.nome, "|", i.cpf, "|", i.data_nascimento, "|", i.salario)

def busca_binaria(nome_arq, cod, tam):
    '''Busca Binaria'''
    left = 0
    right = tam
    while(left <= right):
        middle = int((left+right)//2)
        func = linecache.getline(nome_arq, middle)
        func = func.split("|")
        if int(cod[2:]) == int(func[0]):
            return func
        elif int(func[0]) < int(cod[2:]):
            left = middle + 1
        else:
            right = middle - 1
    return None

def busca_binaria_LUCAS(nome_arq, cod, tam):
    '''Busca Binaria'''
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
            return linha
    return False

#------------------------------------------------------------

aux_dados = Func.Funcionario()
for i in range(100):
        aux_dados.gera_funcionario("data.dat")

funcionarios = []
aux_cod = []
with open("data.dat", "rb+") as arq:
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
    
    #letra c) INICIO
    #Ordena os codigos dos funcionarios, passando-os para uma lista
    start_time = time.time() #Para obter o tempo de execucao
    codigos=[bin(int(ele)) for ele in aux_cod]
    codigos=[int(ele,0) for ele in codigos]
    codigos.sort()
    
    #Apaga todo o conteudo do arquivo
    arq.seek(0)
    arq.truncate()
    
    #Reescreve o arquivo, porem ordenado com base na chave codigo
    j = 0
    i = 0
    while(i < 100 and  j < 100):
        if int(funcionarios[i].cod) == codigos[j]:
            arq.write(str(funcionarios[i].cod).encode())
            arq.write("|".encode())
            arq.write(str(funcionarios[i].nome).encode())
            arq.write("|".encode())
            arq.write(str(funcionarios[i].cpf).encode())
            arq.write("|".encode())
            arq.write(str(funcionarios[i].data_nascimento).encode())
            arq.write("|".encode())
            arq.write(str(funcionarios[i].salario).encode())
            arq.write("|".encode())
            if j < 99:
                arq.write("\n".encode())
            j = j + 1
            i = 0
            continue
        i = i + 1
    
    print("Tempo de Ordernacao: %.10f" % (time.time() - start_time)) #Obtem o tempo de execucao e imprime

    #f = linecache.getline(arq, 50)
    #print(f)

    arq.seek(0, 2)
    tam_arq = arq.tell()
    print("TAMANHO DO ARQUIVO = ", tam_arq)
    arq.seek(0, 0)


print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(aux_dados.busca_sequencial(funcionarios, bin(36)).nome)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

#with open("data.dat", "rb+") as arq:
#particular_line = linecache.getline('data.dat', 50) 
#print(particular_line)

print(busca_binaria_LUCAS("data.dat", 99, 100))


#imprime_funcionarios(funcionarios)
#print("---------------------------------------------------------------------")
#print(codigos)

# print("antes")
# print(aux_cod)
# print("depois")
# codigos.sort()
# print(codigos)



# def sortfunc(funcionario):
#     return funcionario.cod

# sorted(funcionarios, key=sortfunc)

# for i in range(len(funcionarios)):
#     numero = int(funcionarios[i].cod)
#     print(f"func: {numero}")


#for i in funcionarios:
#    print(i.cod, "|", i.nome, "|", i.cpf, "|", i.data_nascimento, "|", i.salario)