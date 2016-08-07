//Felipe Guth - 14210231 - C Code 
//to compile on linux execute the following:  gcc matrixMultiplication.c -o exec -lm
// then execute: ./exec 

#include<stdlib.h>
#include<math.h>
#include<stdio.h>

#define MAX 50


//Read Matrix
void readmatrix(int Mat[MAX][MAX],int row,int col, char name[10])
{ 
int i, j;
printf("\n\n\       Enter the elements of Matrix  %s:\n", name);
for( i= 0; i<=row-1; i++)
for( j= 0; j<=col-1; j++)
{
printf ("\n       %s[%d][%d]:" ,name, i, j);
scanf("%d", &Mat[ i ][ j ]);
}
}


// MULTIPLICATION A X B
void multiplica (int Mata[MAX][MAX], int Matb[MAX][MAX], int ria, int colarib, int colb)
{
int i=0,j=0,k=0;
int C[MAX][MAX];
for(i=0;i<ria;i++) 
{
    for(j=0;j<colb;j++)
    {
        C[i][j] = 0;
        for(k=0;k<colarib;k++) 
        {
                C[i][j] = C[i][j] + Mata[i][k]*Matb[k][j];
        }
    }
}
for( i=0; i<colarib; i++)
for( k=0; k<ria; k++)
printf ("\n Multiplication Result: C[%d][%d]=%d\n",i,k,C[i][k]);
printf("\n");
getchar();
}


main (void) //MAIN MENU *********************************

//Declare variables
{
	int A[MAX][MAX],B[MAX][MAX], coluarowsb=0, rowsa=0, colub=0;
	
	printf("\n\n       Enter the number of rows of matrix A: )");
    scanf("%d",&rowsa);
    printf("\n\n       Enter the number of columns of matrix A and rows of matrix B:");
    scanf("%d",&coluarowsb);
    printf("\n\n       Enter the number of columns of matrix B:");
    scanf("%d",&colub);
    readmatrix(A,rowsa,coluarowsb,"A");
    readmatrix(B,coluarowsb,colub,"B");    
    multiplica(A,B,rowsa,coluarowsb,colub);
	
	
}

