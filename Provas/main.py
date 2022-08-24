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
#------------------------------------------------------------
lista_func = []
fm = Func.Funcionario()

for i in range(100):
    lista_func.append(fm.gera_funcionario("data.dat"))

#lista_func = gera_base_de_dados("data.dat", fm)

print(lista_func)
print("\n\n\n")
lista_func.sort()
print(sorted(lista_func))

print(fm.busca_codigo(lista_func, str(3)))