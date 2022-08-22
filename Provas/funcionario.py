#typedef struct Funcionario {
#int cod;
#char nome[50];
#char cpf[15];
#char data_nascimento[11];
#double salario;
#} TFunc;

class Funcionario:
    def __init__(self, nome, cpf, data_nascimento, salario):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.salario = salario
        