import os
import random
import Function
import cv2
import math
import time
import pickle

random.seed(input('Seed:'))

q = open('./results_final.txt','a+')

#path = '/home/xingjian/Laplacian2-5.0/imgs_data/butterfly_images/50_butterfly/'

path = '/home/rahul/Laplacian2-5.0/imgs_data/cat_images/50_cats/'

store = list() #This list is used to store settings that satisfy psnr > 30dB requirments
children = list() #This list is used to store settings after crossover or mutation
mini_unit_store = list()
mini_unit = list()
num = list()
value = list()
#start_time = time.time()

os.system("make")
for i in range(100):
    count = 0
    Function.writefile()
    arr = Function.readfile()
    for number in range(0,40):
        img = cv2.imread(path+'image'+str(number)+'.jpg')
        height =  img.shape[0]#Get the height of the image
        width = img.shape[1]#get the width of the image
        Function.writefile_0()#make the config.txt all 0.0
        Function.image_print(height,width,number)#get the original image
        os.system('mv /home/rahul/Laplacian2-5.0/imgs/img_out.png /home/rahul/Laplacian2-5.0/imgs/img_out_original.png')#rename the image
        img2= cv2.imread('/home/rahul/Laplacian2-5.0/imgs/img_out_original.png') #It is the orignal image
        Function.wfile(arr)
        Function.image_print(height,width,number) #generate an image that is ready for calculating PSNR
        img1 = cv2.imread('/home/rahul/Laplacian2-5.0/imgs/img_out.png') #read the generated image
        psnr_value = Function.psnr1(img1,img2) #Calculate psnr value
        value.append(psnr_value)
    for x in value:
        if x < 30:
            count = count + 1
    quality_loss = (count/40)*100
    if quality_loss > 5.0:
        value.clear()
        print("next!")
        continue
    elif quality_loss <= 5.0:
        value.clear()
        store.append(arr)
        print("Yes!")
print(store)
mini_unit_store = Function.mini_energy_unit(store) #It is the setting which has minimal energy
ten_units = Function.ten_units(store) #They are settings that have relative minimal energy

rd = random.randint(0,100) #generate a random for probability use
if rd < 90 :
    children = Function.two_points_crossover(ten_units)
    #children = Function.three_points_crossover(ten_units)
if rd >= 90:
    children = Function.two_points_mutation(ten_units)
    #children = Function.three_points_mutation(ten_units)

print("1 time")
time = 1

store.clear()

#The following part will loops through 100 times until getting the best result:
for j in range(100):
    mini_unit.clear() #make the mini_unit array empty
    for k in range(0,90):
        count = 0
        Function.wfile(children[k])
        arr = Function.readfile()
        for number in range(0,40):
            img = cv2.imread(path+'image'+str(number)+'.jpg')
            height =  img.shape[0]#Get the height of the image
            width = img.shape[1]#get the width of the image
            Function.writefile_0()#make the config.txt all 0.0
            Function.image_print(height,width,number)#get the original image
            os.system('mv /home/rahul/Laplacian2-5.0/imgs/img_out.png /home/rahul/Laplacian2-5.0/imgs/img_out_original.png')#rename the image
            img2= cv2.imread('/home/rahul/Laplacian2-5.0/imgs/img_out_original.png') #It is the orignal image
            Function.wfile(arr)
            Function.image_print(height,width,number) #generate an image that is ready for calculating PSNR
            img1 = cv2.imread('/home/rahul/Laplacian2-5.0/imgs/img_out.png') #read the generated image
            psnr_value = Function.psnr1(img1,img2) #Calculate psnr value
            value.append(psnr_value)
        for x in value:
            if x < 30:
                count = count + 1
        quality_loss = (count/40)*100
        if quality_loss > 5.0:
            value.clear()
            print("next!")
            continue
        elif quality_loss <= 5.0:
            value.clear()
            energy = Function.energy(arr)
            percent = Function.percent_error(44326.312,energy)
            q.write("[")
            for item in arr:
                q.write(str(item)+' ')
            q.write("]")
            q.write('\n')
            q.write("The corresponding energy is:" + str(energy) + "fJ\n")
            q.write('The quality loss is:'+str(quality_loss)+'%'+'\n')
            q.write('Compared to the exact setting, this setting will save '+str(percent)+"% energy\n") 
            store.append(arr)
            print("Yes!")

    store = [x for x in store if x != []]
        
    if len(store)<10:
        print("again!")
        continue

    mini_unit = Function.mini_energy_unit(store) #It get the setting which has minimal energ
    mini_energy = Function.energy(mini_unit) #It calculate the minimal energy 
    mini_energy_store = Function.energy(mini_unit_store)
    if mini_energy >= mini_energy_store:

        with open('finalSetting.data', 'wb') as filehandle:
            pickle.dump(mini_unit_store, filehandle)
        #Function.wfile(mini_unit_store)
        #Function.image_print(height,width,number)
        percent = Function.percent_error(44326.312,mini_energy_store)
        #img1 = cv2.imread('/home/xingjian/SobelFilter-master2/imgs/img_out.png')
        #psnr = Function.psnr1(img1,img2)
        f = open('./results.txt',"a+")
        #t = open('./top3.txt','a+')
        print("The best setting is:\n", mini_unit_store)
        print("The corresponding energy is:",mini_energy_store,"J\n")
        print("Compared to exact setting, this setting will save",percent,"% energy\n")
        #print("Its PSNR value is:",psnr,"dB\n")
        #print("The program runs for %s seconds\n" % (time.time() - start_time))
        #second = time.time() - start_time
        #print(ten_units[0])
        #print(ten_units[1])
        #print(ten_units[2])
        #for i in range(0,3):
        #    for item in ten_units[i]:
        #        t.write(str(item)+' ')
        #    t.write('\n')
        #t.close()
        #f.write("It is the image "+ str(number)+"\n")
        f.write("The best setting is:[")
        for item in mini_unit_store:
            f.write(str(item)+' ')
        f.write("]\n")
        f.write("The corresponding energy is:"+str(mini_energy_store)+"J\n")
        f.write("Compared to exact setting, this setting will save "+str(percent)+"% energy\n")
        #f.write("Its PSNR value is:"+str(psnr)+"dB\n")
        #f.write("The program runs for "+ str(second) + " seconds\n")
        f.write("\n")
        j=0
        k=0
        f.close()
        store.clear() #make the store array empty
        break
    elif mini_energy < mini_energy_store:
        mini_energy_store = mini_energy
        mini_unit_store = mini_unit.copy()
        ten_units.clear()
        ten_units = Function.ten_units(store) 
        rd = random.randint(0,100) #generate a random for probability use
        children.clear()
        if rd <= 90 :
            children = Function.two_points_crossover(ten_units)
            #children = Function.three_points_crossover(ten_units)
        if rd >= 91:
            children = Function.two_points_mutation(ten_units)
            #children = Function.three_points_mutation(ten_units)
        store.clear() #make the store array empty
        time = time + 1
        print(time,"time")

print("end\n")
