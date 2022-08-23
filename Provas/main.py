import Funcionario as Func
import names

##arq = open("data.dat", "a+")

lista_func = []
fm = Func.Funcionario()

for i in range(100):
    lista_func.append(fm.gera_funcionario("data.dat"))
    ###arq.seek(0, 2)

print(lista_func)
print("------------------------------------------------------------")

print(fm.busca_codigo(lista_func, str(24)))


#for i in range(100):
#    FuncMain[i].gera_funcionario("data.dat")

#FuncMain[0].gera_funcionario("data.dat")
#FuncMain[1].gera_funcionario("data.dat")
#FuncMain[2].gera_funcionario("data.dat")

###arq.close()