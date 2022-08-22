#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
int main () 
{
    char str1[10], str2[10], str3[10];
    int year;
    FILE * fp;

    fp = fopen ("file.txt", "w+");
    fputw(2, fp);
    fprintf(fp, " ");
    fputw(3, fp);
    
    rewind(fp);
    fscanf(fp, "%s %s %s %d", str1, str2, str3, &year);
    
    printf("Read String1 |%s|\n", str1 );
    printf("Read String2 |%s|\n", str2 );
    printf("Read String3 |%s|\n", str3 );
    printf("Read Integer |%d|\n", year );

    fclose(fp);
    
    return(0);
}
*/


int main ()
{
    printf("start");
    FILE *arq;
    int x = 0, y, aux, i = 0;
    //-----ESCREVENDO TAMANHO DA MATRIZ NO ARQUIVO-----
    arq = fopen("e1_dois.txt", "w+");
    fprintf(arq, "%i %i", 2, 3);

    rewind(arq); //reseta a posição do cursor para o inicio do arquivo
    //------------------------------------------------

    //-----LENDO TAMANHO DA MATRIZ PARA VARIAVEIS-----
    if (arq != NULL)
        fscanf(arq, "%i %i", &x, &y);
    //-----------------------------------------------

    //-----CRIANDO MATRIZ E CHAMANDO FUNCAO-----
    int mat[x][y], j = 0;
    for (int i = 0; i < x; i++)
    { 
        //mat[i][j] = i;
        for (j = 0; j < y; j++)
            mat[i][j] = j;
    }

    /* IMPŔIME MATRIZ
    for (int i = 0; i < x; i++)
    {
        //printf("%i ", mat[i][j]);
        for (int j = 0; j < y; j++)
            printf("%i ", mat[i][j]);
        printf("\n");
    }
    */

    printf("**");

    escreveMat(*mat, x, y);

    printf("((");

    fclose(arq);

    return 0;
}


/*
if (arq != NULL)
    {
        printf("\n@@\n");
        while((fscanf(arq, "%i", &aux))==EOF)
        {
            printf("aux=%i", aux);
            if (x != 0)
                y = aux;
            else    
                x = aux;
            i++;
            if (i >= 1)
                break;
        }
    }
    
*/