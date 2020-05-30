#include "sobel.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#include "macros.h"

//extern char *xconfig_file; //Dongning 20190630: filepath for approximate settings.
//extern bool isApprox; //Dongning 20190630: if using approximate operations.
extern float error[]; 
//extern int cntApprox;//Dongning 20190630: total number of settings.

/*float* xconfig_parse(char* xcfg_file, int cnt) 
{
Dongning 20190630
Function: Read the user-given configuration from file and store the settings (float) into an array for further use.
Arguments:
char* xcfg_file: the file path of the approximate configuration.
int cnt: number of approximate settings, for example, if there are five adders, then this will be 5.

    static float error[cntApprox];
    FILE *approx_adder;
    approx_adder = fopen(xconfig_file,"r");
    if(approx_adder == NULL)
       {
        exit(0);
       }
    while(!feof(approx_adder))
       {
         for(int i=0;i<cntApprox;i++)
          {
            fscanf(approx_adder,"%e",&error[i]);
          }
       }
    fclose(approx_adder);
    return error;
}*/


/*
 * Transforms the rgb information of an image stored in buffer to it's gray
 * representation
 */

int rgbToGray(byte *rgb, byte **gray, int buffer_size) {
    // Take size for gray image and allocate memory
    int gray_size = buffer_size / 3;
    *gray = malloc(sizeof(byte) * gray_size);

    // Make pointers for iteration
    byte *p_rgb = rgb;
    byte *p_gray = *gray;

    // Calculate the value for every pixel in gray
    for(int i=0; i<gray_size; i++) {
        *p_gray = 0.30*p_rgb[0] + 0.59*p_rgb[1] + 0.11*p_rgb[2];

        p_rgb += 3;
        p_gray++;
    }

    return gray_size;
}

/*
 * Make the operation memory for iterative convolution
 */

void makeOpMem(byte *buffer, int buffer_size, int width, int cindex, byte *op_mem) {
    int bottom = cindex-width < 0;
    int top = cindex+width >= buffer_size;
    int left = cindex % width == 0;
    int right = (cindex+1) % width == 0;

    op_mem[0] = !bottom && !left  ? buffer[cindex-width-1] : 0;
    op_mem[1] = !bottom           ? buffer[cindex-width]   : 0;
    op_mem[2] = !bottom && !right ? buffer[cindex-width+1] : 0;

    op_mem[3] = !left             ? buffer[cindex-1]       : 0;
    op_mem[4] = buffer[cindex];
    op_mem[5] = !right            ? buffer[cindex+1]       : 0;

    op_mem[6] = !top && !left     ? buffer[cindex+width-1] : 0;
    op_mem[7] = !top              ? buffer[cindex+width]   : 0;
    op_mem[8] = !top && !right    ? buffer[cindex+width+1] : 0;
}

/*
 *
 *
 given a configuration, e.g., (0, 1, 0, 1, 2, 3, 3, 2, 0, 1, ...., 1, 0, 1), what is the output image? 
 config[] = fopen('config.txt')
 ...
 */

/*
 * Performs convolution between first two arguments
 */
int convolution_h(byte *X, int *Y, int c_size) {
    float sum = 0;
    /*
    for(int i=0; i<c_size; i++) {
        sum += X[i] * Y[c_size-i-1];
    }
    */

    /*generate 8 random numbers for additive approximation purpose*/
    int add_h[8];
    for (int i=0; i<8; i++) {
	 int number = rand() % 10 + 1;
	 add_h[i] = number;
    }

    /*generate 9 random numbers for multiplication approximation purpose*/
    int mult_h[9];
    for (int j=0; j<9; j++) {
         int number = rand() % 10 + 1;
         mult_h[j] = number;
    }


    sum = sum +  X[0] * Y[c_size-1] * (1 + (pow(-1,mult_h[0])) * error[0]);
    /*check sum*/
    sum = (sum + X[1] * Y[c_size-2] * (1 + (pow(-1,mult_h[1])) * error[1])) * (1 + (pow(-1,add_h[0])) * error[18]);
    sum = (sum + X[2] * Y[c_size-3] * (1 + (pow(-1,mult_h[2])) * error[2])) * (1 + (pow(-1,add_h[1])) * error[19]);
    sum = (sum + X[3] * Y[c_size-4] * (1 + (pow(-1,mult_h[3])) * error[3])) * (1 + (pow(-1,add_h[2])) * error[20]);
    sum = (sum + X[4] * Y[c_size-5] * (1 + (pow(-1,mult_h[4])) * error[4])) * (1 + (pow(-1,add_h[3])) * error[21]); 
    sum = (sum + X[5] * Y[c_size-6] * (1 + (pow(-1,mult_h[5])) * error[5])) * (1 + (pow(-1,add_h[4])) * error[22]);
    sum = (sum + X[6] * Y[c_size-7] * (1 + (pow(-1,mult_h[6])) * error[6])) * (1 + (pow(-1,add_h[5])) * error[23]);
    sum = (sum + X[7] * Y[c_size-8] * (1 + (pow(-1,mult_h[7])) * error[7])) * (1 + (pow(-1,add_h[6])) * error[24]);
    sum = (sum + X[8] * Y[c_size-9] * (1 + (pow(-1,mult_h[8])) * error[8])) * (1 + (pow(-1,add_h[7])) * error[25]);
    
    return sum;
}
int convolution_v(byte *X, int *Y, int c_size) {
    float sum = 0;
    /*
    for(int i=0; i<c_size; i++) {
        sum += X[i] * Y[c_size-i-1];
    }
    */
   
    /*generate 8 random numbers for additive approximation purpose*/
    int add_v[8];
    for (int i=0; i<8; i++) {
         int number = rand() % 10 + 1;
         add_v[i] = number;
    }

    /*generate 9 random numbers for multiplication approximation purpose*/
    int mult_v[9];
    for (int j=0; j<9; j++) {
         int number = rand() % 10 + 1;
         mult_v[j] = number;
    }

    sum = sum +  X[0] * Y[c_size-1] * (1 + (pow(-1,mult_v[0])) * error[9]);
    sum = (sum + X[1] * Y[c_size-2] * (1 + (pow(-1,mult_v[1])) * error[10])) * (1 + (pow(-1,add_v[0])) * error[26]);
    sum = (sum + X[2] * Y[c_size-3] * (1 + (pow(-1,mult_v[2])) * error[11])) * (1 + (pow(-1,add_v[1])) * error[27]);
    sum = (sum + X[3] * Y[c_size-4] * (1 + (pow(-1,mult_v[3])) * error[12])) * (1 + (pow(-1,add_v[2])) * error[28]);
    sum = (sum + X[4] * Y[c_size-5] * (1 + (pow(-1,mult_v[4])) * error[13])) * (1 + (pow(-1,add_v[3])) * error[29]);
    sum = (sum + X[5] * Y[c_size-6] * (1 + (pow(-1,mult_v[5])) * error[14])) * (1 + (pow(-1,add_v[4])) * error[30]);
    sum = (sum + X[6] * Y[c_size-7] * (1 + (pow(-1,mult_v[6])) * error[15])) * (1 + (pow(-1,add_v[5])) * error[31]);
    sum = (sum + X[7] * Y[c_size-8] * (1 + (pow(-1,mult_v[7])) * error[16])) * (1 + (pow(-1,add_v[6])) * error[32]);
    sum = (sum + X[8] * Y[c_size-9] * (1 + (pow(-1,mult_v[8])) * error[17])) * (1 + (pow(-1,add_v[7])) * error[33]);

    return sum;
}
/*
 * Iterate Convolution
 */

void itConv_h(byte *buffer, int buffer_size, int width, int *op, byte **res) {
    // Allocate memory for result
    *res = malloc(sizeof(byte) * buffer_size);

    // Temporary memory for each pixel operation
    byte op_mem[SOBEL_OP_SIZE];
    memset(op_mem, 0, SOBEL_OP_SIZE);

    // Make convolution for every pixel
    for(int i=0; i<buffer_size; i++) {
        // Make op_mem
        makeOpMem(buffer, buffer_size, width, i, op_mem);

        // Convolution
        (*res)[i] = (byte) abs(convolution_h(op_mem, op, SOBEL_OP_SIZE));

        /*
         * The abs function is used in here to avoid storing negative numbers
         * in a byte data type array. It wouldn't make a different if the negative
         * value was to be stored because the next time it is used the value is
         * squared.
         */
    }
}
void itConv_v(byte *buffer, int buffer_size, int width, int *op, byte **res) {
    // Allocate memory for result
    *res = malloc(sizeof(byte) * buffer_size);

    // Temporary memory for each pixel operation
    byte op_mem[SOBEL_OP_SIZE];
    memset(op_mem, 0, SOBEL_OP_SIZE);

    // Make convolution for every pixel
    for(int i=0; i<buffer_size; i++) {
        // Make op_mem
        makeOpMem(buffer, buffer_size, width, i, op_mem);

        // Convolution
        (*res)[i] = (byte) abs(convolution_v(op_mem, op, SOBEL_OP_SIZE));
	
	/*
         * The abs function is used in here to avoid storing negative numbers
         * in a byte data type array. It wouldn't make a different if the negative
         * value was to be stored because the next time it is used the value is
         * squared.
         */
   }
}
/*
 * Contour
 */

void contour(byte *sobel_h, byte *sobel_v, int gray_size, byte **contour_img) {
    // Allocate memory for contour_img
    *contour_img = malloc(sizeof(byte) * gray_size);
    
    // Generate a ramdom error
    /* float adder[4] = {0.0,0.004,0.056,0.12};
    int randomIndex = rand() % 4;
    //float randomError = adder[randomIndex];
    float randomError = 0;*/

    // Generate a random number
    int number = rand() % 10 + 1;

    // Iterate through every pixel to calculate the contour image
    for(int i=0; i<gray_size; i++) {
        (*contour_img)[i] = (byte) sqrt((pow(sobel_h[i], 2) + pow(sobel_v[i], 2)) * (1 + (pow(-1,number)) * error[34]));
    }
}

int sobelFilter(byte *rgb, byte **gray, byte **sobel_h_res, byte **sobel_v_res, byte **contour_img, int width, int height) {
    int sobel_h[] = {1, 0, -1, 1, 0, -1, 1, 0, -1},
        sobel_v[] = {1, 1, 1, 0, 0, 0, -1, -1, -1};

    int rgb_size = width*height*3;

    // Get gray representation of the image
    int gray_size = rgbToGray(rgb, gray, rgb_size);

    //Dongning 2019-06-30: User-given approximate (error) settings.
    //xconfig_parse(xconfig_file, cntApprox);
    
    // Make sobel operations
    itConv_h(*gray, gray_size, width, sobel_h, sobel_h_res);
    itConv_v(*gray, gray_size, width, sobel_v, sobel_v_res);

    // Calculate contour matrix
    contour(*sobel_h_res, *sobel_v_res, gray_size, contour_img);

    return gray_size;
}

