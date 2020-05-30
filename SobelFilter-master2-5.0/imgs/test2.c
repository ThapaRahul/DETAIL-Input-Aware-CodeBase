#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void)
{
FILE *approx_adder;
float error[10];
approx_adder = fopen("test2.txt","r");
if(approx_adder == NULL)
{
	exit(0);
}
while(!feof(approx_adder))
{
	for(int i=0;i<10;i++)
	{
    		fscanf(approx_adder,"%e",&error[i]);
        }
}
printf("%e",error[6]);
fclose(approx_adder);
return 0;
}
