#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LSIZ 40
#define RSIZ 10 

int main(void) 
{
    char line[RSIZ][LSIZ];
    char fname[20];
    FILE *fptr = NULL; 
    int i = 0;
    int j = 0;
    int tot = 0; 
    printf(" Input the filename to be opened : ");
    scanf("%s",fname);	

    fptr = fopen(fname, "r");
    while(fgets(line[i], LSIZ, fptr)) 
	{
        line[i][strlen(line[i]) - 1] = '\0';
        i++;
    }
    tot = i;
	printf("\n The content of the file %s  are : \n",fname);    
    for(i = 0; i < tot; ++i)
    {
        printf(" %s\n", line[i]);
    }
    printf("\n");
    return 0;
}
