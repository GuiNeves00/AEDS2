##------------------------------
def Escreve_Matriz(mat, arq):
    arq = open("ex1q2.txt", "a")
    for num in mat:
        arq.write(str(num))
        arq.write("\n")
##------------------------------

arq = open("ex1q2.txt", "w")
integer = 2
arq.write(str(integer))
arq.write(" ")
integer = 3
arq.write(str(integer))
arq.write("\n")

arq = open("ex1q2.txt", "r")

lin = arq.readline(1)
col = arq.readline(2)
mat = [[0 for j in range (int(col))] for i in range(int(lin))]

Escreve_Matriz(mat, arq)

print(arq.read())

arq.close()