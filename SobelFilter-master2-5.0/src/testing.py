import os
import random
import Function
import cv2
import math
import time
import pickle

#path = '/home/rahul/SobelFilter-master2/imgs_data/cat_images/50_cats/'
path = '/home/rahul/SobelFilter-master2-5.0/imgs_data/butterfly_images/50_butterfly/'
#path = '/home/rahul/SobelFilter-master2/imgs_data/butterfly_images/50_butterfly/'

# creating a test finalsetting.data file

'''
mini_unit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open('finalSetting.data', 'wb') as filehandle:
	pickle.dump(mini_unit, filehandle)

'''

#with open('finalSetting.data', 'rb') as filehandle:
#    arr = pickle.load(filehandle)


arr = [0.00072, 0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072,0.00072, 0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004]
#arr = [0.0024, 0.024, 0.00072, 0.00072, 0.024, 0.0024, 0.0024, 0.024, 0.0024, 0.0024, 0.0024, 0.0024, 0.024, 0.024, 0.024, 0.00072, 0.0024, 0.0024, 0.056, 0.004, 0.056, 0.004, 0.0, 0.0, 0.004, 0.0, 0.0, 0.0, 0.0, 0.004, 0.004, 0.004, 0.004, 0.004, 0.004 ]

#arr = [0.0024, 0.024, 0.00072, 0.00072, 0.024, 0.0024, 0.0024, 0.024, 0.0024, 0.0024, 0.0024, 0.0024, 0.024, 0.024, 0.024, 0.00072, 0.0024, 0.0024, 0.12, 0.004, 0.12, 0.004, 0.0, 0.0, 0.004, 0.0, 0.0, 0.0, 0.0, 0.004, 0.004, 0.004, 0.004, 0.004, 0.004 ]

value = []

os.system("make")
for number in range(0,40):
    img = cv2.imread(path+'image'+str(number)+'.jpg')
    height =  img.shape[0]#Get the height of the image
    width = img.shape[1]#get the width of the image
    Function.writefile_0()#make the config.txt all 0.0
    Function.image_print(height,width,number)#get the original image
    os.system('mv /home/rahul/SobelFilter-master2-5.0/imgs/img_out.png /home/rahul/SobelFilter-master2-5.0/imgs/img_out_original.png')#rename the image
    img2= cv2.imread('/home/rahul/SobelFilter-master2-5.0/imgs/img_out_original.png') #It is the orignal image
    Function.wfile(arr)
    Function.image_print(height,width,number) #generate an image that is ready for calculating PSNR
    img1 = cv2.imread('/home/rahul/SobelFilter-master2-5.0/imgs/img_out.png') #read the generated image
    psnr_value = Function.psnr1(img1,img2) #Calculate psnr value
    value.append(psnr_value)

f = open('./testResults.txt',"a+")
count = 0
f.write("[")
for x in value:
    f.write(str(x)+' ')
    if x < 30:
        count = count + 1
f.write("]")
f.write('\n')
quality_loss = (count/40)*100
energy = Function.energy(arr)
percent = Function.percent_error(88658.413,energy)
f.write("The corresponding energy is:"+str(energy)+"J\n")
f.write("Compared to exact setting, this setting will save "+str(percent)+"% energy\n")
f.write("The quality loss is " + str(quality_loss) + "%\n")
f.write("\n")
f.close()



	




