#include <stdio.h>
#include <stdlib.h>

int main ()
{
    /*FILE *arq;
    int vet[5] = {2, 4, 6, 8, 10};
    arq = fopen("teste.txt", "w");
    if(arq != NULL) 
    {
        int i;
        for (i=0; i < 5; i++)
        {
            fprintf(arq, "%d\n", vet[i]);
        }
        fclose(arq);
    }

    /*FILE *arq;
    int i;
    arq = fopen("teste.txt", "r");
    if (arq != NULL)
    {
        while((fscanf(arq, "%i \n", &i)) != EOF)
        {
            printf("%i \n", i);
        }
        fclose(arq);
    }*/

    //ARQUIVO BINARIO
    /*
    FILE *arq;
    int vet[5] = {2, 4, 6, 8, 10};
    arq = fopen("teste.dat", "wb");
    if (arq != NULL)
    {
        fwrite(vet, sizeof(int), 5, arq);
    }
    fclose(arq);
    */

    //ACESSO SEQUENCIAL
    FILE *arq;
    int vet[5], i = 0;
    arq = fopen("teste.dat", "rb");
    if (arq != NULL)
    {
        while (fread(&vet[i], sizeof(int), 1, arq) == 1)
        {
            printf("%d \n", vet[i]);
            i++;
        }
    }
    for (int i = 0; i < 5; i++)
    {
        printf("%d", vet[i]);
    }
    fclose(arq);
}