#typedef struct Funcionario {
#int cod;
#char nome[50];
#char cpf[15];
#char data_nascimento[11];
#double salario;
#} TFunc;

import names
import random

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
        arq_funcao.seek(0, 2)
        #cod
        self.cod = random.choice(self.rnd_array) #escolhe um valor aleatorio do vetor rnd_array
        self.rnd_array.remove(self.cod) #remove este valor do vetor rnd_array para que nao haja codigos repetidos
        #self.cod = str(random.randint(0, 99))  #versao antiga
        arq_funcao.write(bin(self.cod)[2:].encode()) 
        arq_funcao.write("|".encode())
        #nome
        self.nome = (names.get_full_name()) 
        arq_funcao.write(self.nome.encode())
        arq_funcao.write("|".encode())
        #cpf
        self.cpf = (str(random.randint(10000000000, 99999999999)))
        arq_funcao.write(self.cpf.encode())
        arq_funcao.write("|".encode())
        #data_nascimento
        self.data_nascimento = (str(random.randint(1, 31)) + "/" + str(random.randint(1, 12)) + "/" + str(random.randint(1930, 2022)))
        arq_funcao.write(self.data_nascimento.encode())
        arq_funcao.write("|".encode())
        #salario
        self.salario = (str(random.randint(1200, 100000)))
        arq_funcao.write(self.salario.encode())
        arq_funcao.write("|".encode())
        #fim do registro
        aux = str(str(self.cod)+"|"+self.nome+"|"+self.cpf+"|"+self.data_nascimento+"|"+self.salario) #str(self.cod) pq sem isso acusou erro
        arq_funcao.write("\n".encode())
        arq_funcao.seek(0, 2)
        arq_funcao.close()
        return aux


    #letra b)
    def busca_codigo(self, lista, cod):
        comparacoes = 0
        for i in range(100):
            if cod == lista[i][:2]:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Dados do funcionario: ", lista[i], "\nTotal de comparacoes: ", comparacoes)
                return lista[i]
            else:
                comparacoes = comparacoes + 1

            #arq_funcao.write(names.get_full_name() + "@") #nome
            #arq_funcao.write(str(random.randint(10000000000, 99999999999))) #cpf
            #arq_funcao.write = (str(random.randint(1, 31)) + str(random.randint(1, 12)) + str(random.randint(1930, 2022))) #data_nascimento
            #arq_funcao.write = (str(random.randint(1200, 100000))) #salario