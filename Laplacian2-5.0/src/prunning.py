import os
import Function
import cv2
import numpy as np
import math
f = open('./PSNR.txt','a+')
path = '/home/rahul/Laplacian2-5.0/imgs_data/butterfly_images/50_butterfly'
os.system("make")
value = list()
for i in range(9,17):
    count = 0
    for number in range(0,30):
        img = cv2.imread(path+'/image'+str(number)+'.jpg')
        height =  img.shape[0]
        width = img.shape[1]
        
        Function.writefile_0()

        Function.image_print(height,width,number)
        os.system('mv /home/rahul/Laplacian2-5.0/imgs/img_out.png /home/rahul/Laplacian2-5.0/imgs/img_out_original.png')
        img2= cv2.imread('/home/rahul/Laplacian2-5.0/imgs/img_out_original.png') #It is the orignal image

        #Function.writefile_n()
        #array = Function.readfile_t()
        #Function.wfile(array[i])
        Function.writefile_t(i)
        Function.image_print(height,width,number)
        img1 = cv2.imread('/home/rahul/Laplacian2-5.0/imgs/img_out.png') #read the generated image
        PSNR = Function.psnr1(img1,img2)
        value.append(PSNR)
    for x in value:
        if x < 30:
            count = count + 1
    for item in value:
        f.write(str(item)+' ')
    f.write('\n')
    quality_loss = (count/30)*100
    f.write('The quality loss is:'+str(quality_loss)+'%'+'\n')
    print(quality_loss)
    value.clear()
f.close()
