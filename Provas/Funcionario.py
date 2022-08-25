#typedef struct Funcionario {
#int cod;
#char nome[50];
#char cpf[15];
#char data_nascimento[11];
#double salario;
#} TFunc;

import names
import random
import time

class Funcionario:
    def __init__(self, cod = 0, nome = None, cpf = 0, data_nascimento = 0, salario = 0):
        self.cod = 0 
        self.nome = 0
        self.cpf = 0
        self.data_nascimento = 0
        self.salario = 0

    rnd_array = [i for i in range(100)] #vetor para gerar codigos aleatorios

    #letra a)
    def gera_funcionario(self, nome_arq):
        aux = 0
        arq_funcao = open(nome_arq, "rb+")
        arq_funcao.seek(0, 2) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FIX

        #cod
        self.cod = random.choice(self.rnd_array) #escolhe um valor aleatorio do vetor rnd_array
        self.rnd_array.remove(self.cod) #remove este valor do vetor rnd_array para que nao haja codigos repetidos
        #self.cod = str(random.randint(0, 99))  #versao antiga
        arq_funcao.write(bin(self.cod)[2:].encode()) #[2:] para retirar o indicador de binario (0b)
        arq_funcao.write("|".encode())

        #nome
        self.nome = (names.get_full_name()) 
        arq_funcao.write(self.nome.encode())
        arq_funcao.write("|".encode())

        #cpf
        self.cpf = (random.randint(10000000000, 99999999999))
        arq_funcao.write(bin(self.cpf)[2:].encode())
        arq_funcao.write("|".encode())

        #data_nascimento
        dn_dia = random.randint(1, 31)
        dn_mes = random.randint(1, 12)
        dn_ano = random.randint(1930, 2022)
        arq_funcao.write(bin(dn_dia)[2:].encode())
        arq_funcao.write("/".encode())
        arq_funcao.write(bin(dn_mes)[2:].encode())
        arq_funcao.write("/".encode())
        arq_funcao.write(bin(dn_ano)[2:].encode())
        arq_funcao.write("|".encode())
        self.data_nascimento = str(dn_dia) + "/" + str(dn_mes) + "/" + str(dn_ano)

        #self.data_nascimento = (str(random.randint(1, 31)) + "/" + str(random.randint(1, 12)) + "/" + str(random.randint(1930, 2022)))
        #arq_funcao.write(self.data_nascimento.encode())
        #arq_funcao.write("|".encode())

        #salario
        self.salario = (random.randint(1200, 100000))
        arq_funcao.write(bin(self.salario)[2:].encode())
        arq_funcao.write("|".encode())

        #fim do registro
        aux = str(str(self.cod)+"|"+str(self.nome)+"|"+str(self.cpf)+"|"+str(self.data_nascimento)+"|"+str(self.salario)) #str(self.cod) pq sem isso acusou erro
        arq_funcao.write("\n".encode())
        arq_funcao.seek(0, 2)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FIX
        arq_funcao.close()
        return aux

    #letra b) ATUALIZADA
    def busca_sequencial(self, funcionarios, cod):
        '''Recebe uma lista de objetos funcionario NÃO ORDENADA por nenhuma chave, um codigo em binario, faz a busca pelo funcionario deste codigo e o retorna (objeto)'''
        start_time = time.time()
        comparacoes = 0
        cod = cod[2:]
        for i in range(100):
            if funcionarios[i].cod == cod:
                print("Tempo gasto: %.10f" % (time.time() - start_time), "Comparacoes feitas: ", comparacoes)
                return funcionarios[i]
            comparacoes = comparacoes + 1


    #letra b) ANTIGA
    # def busca_codigo(self, lista, cod: str):
    #     #cod = cod[2:] #retira sufixo indicativo de binario 0b||1b
    #     comparacoes = 0
    #     start_time = time.time() #Inicia o timer para contar o tempo de execucao do algoritmo
        
    #     for i in range(100):
    #         #if "|" in lista[i][1]: #checa se o numero eh de um digito e faz a correcao de busca
    #         #    if cod == lista[i][0]:
    #         #        print("Dados do funcionario: ", lista[i], "\nTotal de comparacoes: ", comparacoes, "\nTempo gasto: %.10f" % (time.time() - start_time))
    #         #        return lista[i]
    #         if cod == lista[i][:2]:
    #             print(lista[i][:2])
    #             print("Dados do funcionario: ", lista[i], "\nTotal de comparacoes: ", comparacoes, "\nTempo gasto: %.10f" % (time.time() - start_time))
    #             return lista[i]
    #         else:
    #             comparacoes = comparacoes + 1
    #         if i == 99:
    #             return "Codigo de funcionario invalido ou inexistente!"