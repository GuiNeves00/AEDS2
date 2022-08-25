import linecache
from posixpath import split
from tracemalloc import start
import Funcionario as Func
import time
import os

#FUNCOES-----------------------------------------------------
def gera_base_de_dados(nome_arq, obj):
    lista = []
    if os.stat(nome_arq).st_size > 0:
        print("Base de dados ja foi criada anteriormente!!")
        opcao = int(input(print("Digite:\n1 = Criar nova base de dados\n2 = Finalizar programa")))
        if opcao == 1:
            f = open(nome_arq, "r+")
            f.seek(0)
            f.truncate()
            f.close()
            
            for i in range(100):
                lista.append(obj.gera_funcionario(nome_arq))
                return lista
        if opcao == 2:
            exit()
    #else:
        #for i in range(100):
            #lista.append(obj.gera_funcionario(nome_arq))
    #return lista

def imprime_funcionarios(funcionarios):
    for i in funcionarios:
        print(i.cod, "|", i.nome, "|", i.cpf, "|", i.data_nascimento, "|", i.salario)

def busca_binaria(cod, arq, tam):
    arq.seek(0, 0)
    cima = 0
    baixo = tam-1
    print("cod = ", cod)
    while(cima <= baixo):
        print("cima = ", cima, "baixo = ", baixo)
        meio = round((cima+baixo)/2)
        print("meio = ", meio)
        #arq.seek(int(meio), 0)
        f = arq.readlines()
        print("f antes = ", f)
        aux_f = f.split("|")
        print("aux_f = ", aux_f)
        #print("f[0][2:] = ", f[0][2:])
        if cod == f[0][2:]:
            return f
        elif cod > f[0][2:]:
            cima = meio + 1
        else:
            baixo = meio - 1
    
    return "chegou no return final"

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
    print(busca_binaria(bin(36), arq, 100))


print(aux_dados.busca_sequencial(funcionarios, bin(36)).nome)






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