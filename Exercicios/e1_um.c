#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main ()
{
    FILE *arq;
    int cont = 0;
    char aux;
    char string[50] = "exercicio 1 questao numero 1";

    arq = fopen("e1_um.txt", "w");

    for (int i = 0; i < strlen(string); i++)
        fprintf(arq, "%c", string[i]);

    fclose(arq);

    //-------------------------------------------------------
    arq = fopen("e1_um.txt", "r");
    printf("lendo arquivo...\n");

    if (arq != NULL)
        while((fscanf(arq, "%c", &aux)) != EOF)
            if (aux == 32)
                cont++;

    printf("\ntotal de espacos em branco = %i\n", cont);
    fclose(arq);

    return 0;
}