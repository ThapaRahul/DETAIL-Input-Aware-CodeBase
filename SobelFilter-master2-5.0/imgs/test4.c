#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
void test()
{
    printf("Hello\n");
}
int main()
{
srand(time(0));
test();
int sign_h[8];
for (int i=0; i<8; i++) {
         int number = rand() % 10 + 1;
         sign_h[i] = number;
  }
int i = 0;
int j = 0;
j = pow(-1,sign_h[0]) + 10 ;
printf("%i\n",j);
return 0;
}
