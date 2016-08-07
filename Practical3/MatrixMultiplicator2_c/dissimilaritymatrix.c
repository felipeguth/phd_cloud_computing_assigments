//Felipe Guth - 14210231 - C Code
//to compile on linux execute the following:  gcc dissimilarityMatrix.c -o exec -lm
// then execute: ./exec 

#include<stdlib.h>
#include<math.h>
#include<stdio.h>

#define MAX 10

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


main()
{
	int A[MAX][MAX] = {{0}}, n=0, p=0, no=1,ne=0, aux=0, val=0,cont=0, i=0, j=0;
	float vet[MAX]={{0}}, D[MAX][MAX]={{0}};
	
	
	printf("\n\n       Enter the number of objects of : )");
	scanf("%d",&n);
	printf("\n\n       Enter the number of dimensions of each object: )");
	scanf("%d",&p);
	
	readmatrix(A,n,p,"A");
		
	//calculate the dissimilarity vector	
	for(no=1;no<n;no++)
	{			
		for(aux=0;aux!=no;aux++) 
		{ 
							
			val = 0;	
			for(ne=0;ne<=p-1;ne++)
			{
				val = val + (A[no][ne]-A[aux][ne])*(A[no][ne]-A[aux][ne]);				
			}
			vet[cont] = sqrt(val);
			cont++;
		
		}
	}
	
	//build dissimilarity matrix
	cont = 0;
	for(i=1;i<=n;i++)
	{
		for(j=0;j!=i;j++)
		{
			D[i][j] = vet[cont];			
			cont++;			
		}		
	}
	
	//Show matrix
	for( i=0; i<n; i++)
		for( j=0; j<n; j++)
			printf ("\n Dissimilarity Result: D[%d][%d]= %.2f \n",i,j,D[i][j]);
	printf("\n");
	getchar();
		
}//end
