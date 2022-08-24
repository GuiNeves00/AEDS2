from posixpath import split
import Funcionario as Func
import names
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

    #Ordena os codigos dos funcionarios, passando-os para uma lista
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
        #print("func.cod: ", funcionarios[i].cod, "cod_ord: ", codigos[j])
        print("i = ", i, "j = ", j)
        if int(funcionarios[i].cod) == codigos[j]:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
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

imprime_funcionarios(funcionarios)
print("---------------------------------------------------------------------")
print(codigos)

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