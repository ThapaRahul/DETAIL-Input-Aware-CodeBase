#include "sobel.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include "macros.h"

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


//read the configuration file and return the configuration into an array 
void read_config(){
   
 
}

/*
 * Performs convolution between first two arguments
 */

int convolution_h(byte *X, int *Y, int c_size) {
    int sum = 0;
    /*
    for(int i=0; i<c_size; i++) {
        sum += X[i] * Y[c_size-i-1];
    }
    */

    /*generate 8 random numbers for approximation purpose*/
    float adder[4] = {0.0,0.004,0.056,0.12};
    float error[8];
    for (int i=0; i<8; i++) {
	 int randomIndex = rand() % 2;
	 float randomValue = adder[randomIndex];
	 error[i] = randomValue;
    }

    /*no error for the first one*/
    sum = sum + X[0] * Y[c_size-1];
    sum = (sum + X[1] * Y[c_size-2]) * (1 + error[0]);
    sum = (sum + X[2] * Y[c_size-3]) * (1 + error[1]);
    sum = (sum + X[3] * Y[c_size-4]) * (1 + error[2]);
    sum = (sum + X[4] * Y[c_size-5]) * (1 + error[3]); 
    sum = (sum + X[5] * Y[c_size-6]) * (1 + error[4]);
    sum = (sum + X[6] * Y[c_size-7]) * (1 + error[5]);
    sum = (sum + X[7] * Y[c_size-8]) * (1 + error[6]);
    sum = (sum + X[8] * Y[c_size-9]) * (1 + error[7]);
    
    return sum;
}
int convolution_v(byte *X, int *Y, int c_size) {
    int sum = 0;
    /*
    for(int i=0; i<c_size; i++) {
        sum += X[i] * Y[c_size-i-1];
    }
    */
   
    /*generate 8 random numbers for approximation purpose*/
    float adder[4] = {0.0,0.004,0.056,0.12};
    float error[8];
    for (int i=0; i<8; i++) {
         int randomIndex = rand() % 2;
         float randomValue = adder[randomIndex];
    /*random -1 or 1*/
    	 //error[i] = pow((-1), )randomValue;
    	 error[i] = randomValue;
    }

    /*no error for the first one*/
    sum = sum + X[0] * Y[c_size-1];
    sum = (sum + X[1] * Y[c_size-2]) * (1 + error[0]);
    sum = (sum + X[2] * Y[c_size-3]) * (1 + error[1]);
    sum = (sum + X[3] * Y[c_size-4]) * (1 + error[2]);
    sum = (sum + X[4] * Y[c_size-5]) * (1 + error[3]);
    sum = (sum + X[5] * Y[c_size-6]) * (1 + error[4]);
    sum = (sum + X[6] * Y[c_size-7]) * (1 + error[5]);
    sum = (sum + X[7] * Y[c_size-8]) * (1 + error[6]);
    sum = (sum + X[8] * Y[c_size-9]) * (1 + error[7]);

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
    float adder[4] = {0.0,0.004,0.056,0.12};
    int randomIndex = rand() % 4;
    //float randomError = adder[randomIndex];
    float randomError = 0;

    // Iterate through every pixel to calculate the contour image
    for(int i=0; i<gray_size; i++) {
        (*contour_img)[i] = (byte) sqrt((pow(sobel_h[i], 2) + pow(sobel_v[i], 2)) * (1 + randomError));
    }
}

int sobelFilter(byte *rgb, byte **gray, byte **sobel_h_res, byte **sobel_v_res, byte **contour_img, int width, int height) {
    int sobel_h[] = {-1, 0, 1, -2, 0, 2, -1, 0, 1},
        sobel_v[] = {1, 2, 1, 0, 0, 0, -1, -2, -1};

    int rgb_size = width*height*3;

    // Get gray representation of the image
    int gray_size = rgbToGray(rgb, gray, rgb_size);

    // Make sobel operations
    itConv_h(*gray, gray_size, width, sobel_h, sobel_h_res);
    itConv_v(*gray, gray_size, width, sobel_v, sobel_v_res);

    // Calculate contour matrix
    contour(*sobel_h_res, *sobel_v_res, gray_size, contour_img);

    return gray_size;
}

