import random
import os
import cv2
import numpy as np
import math

def percent_error(exact,approx):
    percent_error=abs((exact-approx)/exact)*100
    return percent_error

def energy(omega):
    energy=0
    mult = list()
    add = list()
    mult_e = omega[:18]
    add_e = omega[18:]
    for item in mult_e:
        if item == 0.0:
            energy = energy + 4920
        elif item == 0.00072:
            energy = energy + 1000
        elif item == 0.0024:
            energy = energy + 930
        elif item == 0.008:
            energy = energy + 740
        elif item == 0.024:
            energy = energy + 590
    for number in add_e:
        if number == 0.0:
            energy = energy + 5.789
        elif number == 0.004:
            energy = energy + 1.906
        elif number == 0.056:
            energy = energy + 1.815
    return energy

def energy_test(omega):
    energy=0
    count=0
    for j in range(0,18):
        if omega[j]==0.0:
            energy=energy+4920
        elif omega[j]==0.00072:
            energy=energy+1000
        elif omega[j]==0.0024:
            energy=energy+930
        elif omega[j]==0.008:
            energy=energy+740
        elif omega[j]==0.024:
            energy=energy+590
    for i in range(18,35):
        if omega[i]==0.0:
            energy=energy+5.789
        elif omega[i]==0.004:
            energy=energy+1.906
        elif omega[i]==0.056:
            energy=energy+1.815
    return energy

def crossover(cross):
    cross_new=[ ]
    mid=[ ]
    for i in range(0,10):
        mid=cross[i].copy()
        for j in range(0,10):
            if i!=j:
                rd = random.randint(0,6)
                cross[i][rd]=cross[j][rd]
                cross_new.append(cross[i].copy())
                cross[i]=mid.copy()
    return cross_new

def two_points_crossover(cross):
    size = len(cross)
    #print(size)
    #print(cross)
    cross_new=[ ]
    mid=[ ]
    for i in range(0,10):
        mid=cross[i].copy()
        for j in range(0,10):
            if i!=j:
                rd = random.randint(0,17)
                rp = random.randint(19,34)
                
                first = cross[j][rd]
                cross[i][rd] = first
                second = cross[j][rp]
                cross[i][rp] = second
                
                cross_new.append(cross[i].copy())
                cross[i]=mid.copy()
            else:
                continue
    #print(len(cross_new))
    return cross_new

def two_points_mutation(muta):
    mult = [0.0,0.00072]
    adder = [0.0,0.004]
    store_mu = list()
    for i in range(0,10):
        rd = random.randint(0,17)
        rp = random.randint(19,34)
        muta[i][rd]=random.choice(mult)
        muta[i][rp]=random.choice(adder)
    for j in range(0,80):
        for k in range(18):
            mul_m = random.choice(mult)
            store_mu.append(mul_m)
        for l in range(17):
            add_m = random.choice(adder)
            store_mu.append(add_m)
        muta.append(store_mu)
        store_mu.clear()
    return muta

def three_points_crossover(cross):
    cross_new=[ ]
    mid=[ ]
    for i in range(0,10):
        mid=cross[i].copy()
        for j in range(0,10):
            if i!=j:
                rd = random.randint(0,10)
                rs = random.randint(11,17)
                rp = random.randint(18,34)
                if rd != rp:
                    cross[i][rd]=cross[j][rd]
                    cross[i][rp]=cross[j][rp]
                    cross[i][rs]=cross[j][rs]
                if rd == rp:
                    cross[i][rd]=cross[j][rd]
                cross_new.append(cross[i].copy())
                cross[i]=mid.copy()
    return cross_new

def three_points_mutation(muta):
    mult = [0.0,0.00072]
    adder = [0.0,0.004]
    store = list()
    for i in range(0,10):
        rd = random.randint(0,10)
        rs = random.randint(11,17)
        rp = random.randint(18,34)
        muta[i][rd]=random.choice(mult)
        muta[i][rs]=random.choice(mult)
        muta[i][rp]=random.choice(adder)
    for j in range(0,80):
        for k in range(18):
            mul = random.choice(mult)
            store.append(mul)
        for l in range(17):
            add = random.choice(adder)
            store.append(add)
        muta.append(store)
        store[:] = [ ]
    return muta

def four_points_crossover(cross):
    cross_new=[ ]
    mid=[ ]
    for i in range(0,10):
        mid=cross[i].copy()
        for j in range(0,10):
            if i!=j:
                rd = random.randint(0,10)
                rs = random.randint(11,17)
                rp = random.randint(18,25)
                rl = random.randint(26,34)
                if rd != rp:
                    cross[i][rd]=cross[j][rd]
                    cross[i][rp]=cross[j][rp]
                    cross[i][rs]=cross[j][rs]
                    cross[i][rl]=cross[j][rl]
                if rd == rp:
                    cross[i][rd]=cross[j][rd]
                cross_new.append(cross[i].copy())
                cross[i]=mid.copy()
    return cross_new

def four_points_mutation(muta):
    mult = [0.0,0.00072]
    adder = [0.0,0.004]
    store = list()
    for i in range(0,10):
        rd = random.randint(0,10)
        rs = random.randint(11,17)
        rp = random.randint(18,25)
        rl = random.randint(26,34)
        muta[i][rd]=random.choice(mult)
        muta[i][rs]=random.choice(mult)
        muta[i][rp]=random.choice(adder)
        muta[i][rl]=random.choice(adder)
    for j in range(0,80):
        for k in range(18):
            mul = random.choice(mult)
            store.append(mul)
        for l in range(17):
            add = random.choice(adder)
            store.append(add)
        muta.append(store)
        store[:] = [ ]
    return muta

def mini_energy_unit_test(unit):
    size = len(unit)
    mini_energy=186973
    mini_unit=[ ]
    for i in range(0,size):
        if i!=size-1:
            energy1=energy(unit[i])
            energy2=energy(unit[i+1])
        if energy2<energy1 and energy2<mini_energy:
            mini_energy=energy2
            mini_unit=unit[i+1].copy()
    return mini_unit

def mini_energy_unit(unit):
    mini_energy = 186973
    mini_unit = list()
    for item in unit:
        if energy(item) < mini_energy:
            mini_energy = energy(item)
            mini_unit = item.copy()
    return mini_unit

def ten_units(unit):
    rela_energy = 186973
    rela_unit = list()
    ten_units = list()
    for i in range(10):
        for item in unit:
            if energy(item) < rela_energy:
                rela_energy = energy(item)
                rela_unit = item.copy()
        ten_units.append(rela_unit)
        unit.remove(rela_unit)
        rela_energy = 186973
    return ten_units

def ten_units_test(step1):
#Sort together and use a for loop
    count=0
    ten_unit=[ ]
    rela_unit=[ ]
    rela_energy=186973
    x=0
    size=len(step1)

            
    for l in range(10):
        for k in range(0,size-x):
            if k!=size-1-x:
                energy3=energy(step1[k])
                energy4=energy(step1[k+1])
            if energy4<=energy3 and energy4<rela_energy:
                rela_energy=energy4
                rela_unit=step1[k+1].copy()
                count=k+1
            else:
                continue
        ten_unit.append(rela_unit)
        del step1[count]
        rela_energy=186973
        k=0
        x=x+1
    return ten_unit

def image_print(height,width,num):
    #os.system("make")
    
    #os.system("convert ../imgs/img.png ../imgs/img.rgb")
    #os.system("./../src/sobel ../imgs/img.rgb ../imgs/img_out.gray 512x512 -g ../imgs/img_out_gray.gray -i ../imgs/img_out_h.gray ../imgs/img_out_v.gray -x ../src/config.txt 35")
    #os.system("convert -size 512x512 -depth 8 ../imgs/img_out.gray ../imgs/img_out.png")
    
    #stri1 = 'convert ../imgs_data/cat_images/50_cats/image'
    stri1 = 'convert ../imgs_data/butterfly_images/50_butterfly/image'
    #stri1 = 'convert ../imgs_data/cat_butterfly_images/50_cats_butterfly/image'
    stri2 = '.jpg ../imgs/img.rgb'
    string_0 = stri1 + str(num) + stri2
    os.system(string_0)

    #os.system("convert ../imgs_data/Val_images/val2017/image0.jpg ../imgs/img.rgb")
    string1 = './../src/sobel ../imgs/img.rgb ../imgs/img_out.gray '
    string2 = 'x'
    string3 = ' -g ../imgs/img_out_gray.gray -i ../imgs/img_out_h.gray ../imgs/img_out_v.gray -x ../src/config.txt 35'
    string_1 = string1 + str(width) + string2 + str(height)+ string3
    os.system(string_1)
    
    string4 = 'convert -size '
    string5 = ' -depth 8 ../imgs/img_out.gray ../imgs/img_out.png'
    string_2=(string4 + str(width) + string2 + str(height) + string5)
    os.system(string_2)

def readfile():
    f = open('./config.txt','r')
    words = list()
    for line in f:
        line = line.rstrip()
        words = line.split()
    for i in range(len(words)):
        words[i]=float(words[i])
    f.close()
    return words

def readfile_t():
    f = open('./top3.txt','r')
    words = list()
    arr= list()
    for line in f:
        line = line.rstrip()
        words = line.split()
        for i in range(len(words)):
            words[i]=float(words[i])
        arr.append(words)
    f.close()
    return arr

def writefile_0():
    f = open('./config.txt','w')
    for i in range(35):
        f.write(str(0.0)+' ')
    f.close()


"""
# Training on cats_butterfly images and testing on dogs images
def writefile():
    f = open('./config.txt','w')
    omega = list()

    # Multiplies Customization
    mult = [0.0, 0.00072, 0.0024, 0.008, 0.024]
    mult1 = 0.0
    mult2 = [0.0, 0.00072]
    mult3 = [0.0, 0.00072, 0.0024]
    mult4 = [0.0, 0.00072, 0.0024, 0.008]
    for i in range(18):
        omega.append(random.choice(mult2))
    omega[1] = 0.024
    omega[3] = 0.0
    omega[4] = 0.024
    omega[7] = 0.024
    omega[12] = 0.024
    omega[13] = 0.024
    omega[14] = 0.024

    # Adders Customization
    adder = [0.0, 0.004, 0.056, 0.12]
    adder2 = [0.0, 0.004]
    for j in range(17):
        omega.append(0.0)
    #omega[18] = random.choice(adder2)
    #omega[19] = random.choice(adder2)
    #omega[20] = random.choice(adder2)
    #omega[21] = random.choice(adder2)
    #omega[22] = random.choice(adder2)
    omega[34] = random.choice(adder2)
    
    for item in omega:
        f.write(str(item)+' ')
    f.close()

"""

#Training on cats images
def writefile():
    f = open('./config.txt','w')
    omega = list()

    # Multiplies Customization
    mult = [0.0, 0.00072, 0.0024, 0.008, 0.024]
    mult1 = 0.0
    mult2 = [0.0, 0.00072]
    mult3 = [0.0, 0.00072, 0.0024]
    mult4 = [0.0, 0.00072, 0.0024, 0.008]
    for i in range(18):
        omega.append(random.choice(mult3))
    omega[1] = 0.024
    omega[4] = 0.024
    omega[7] = 0.024
    omega[12] = 0.024
    omega[13] = 0.024
    omega[14] = 0.024

    # Adders Customization
    adder = [0.0, 0.004, 0.056, 0.12]
    adder2 = [0.0, 0.004]
    for j in range(17):
        omega.append(random.choice(adder2))
    omega[27] = 0.0
    omega[28] = 0.0
    omega[29] = 0.0
    omega[30] = 0.0
    
    for item in omega:
        f.write(str(item)+' ')
    f.close()
	
"""
Original prunning for training and testing on butterfly images
def writefile():
    f = open('./config.txt','w')
    omega = list()
    mult = [0.0,0.00072]
    for i in range(18):
        omega.append(random.choice(mult))
    omega[1] = 0.024
    omega[4] = 0.024
    omega[7] = 0.024
    omega[12] = 0.024
    omega[13] = 0.024
    omega[14] = 0.024
    adder = [0.0,0.004]
    for j in range(17):
        omega.append(0.0)
    omega[18] = random.choice(adder)
    omega[19] = random.choice(adder)
    omega[22] = random.choice(adder)
    #omega[34] = random.choice(adder)
    for item in omega:
        f.write(str(item)+' ')
    f.close()
"""

def writefile_n():
    f = open('./config.txt','w')
    new = [0.0024,0.024,0.0024,0.0024,0.024,0.0024,0.0024,0.024,0.0024,0.0024,0.0024,0.0024,0.024,0.024,0.024,0.0024,0.0024,0.0024,0.004,0.004,0.0,0.0,0.004,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.004]
    print(len(new))
    for item in new:
        f.write(str(item)+' ')
    f.close()

def writefile_t(i):
    f = open('./config.txt','w')
    test = list()
    n=35
    m=0
    zero=[0.0*m for q in range(n)]
    test=zero.copy()
    test[i] = 0.004
    #test[34] = 0.056
    #test[34] = 0.004
    #test[20] = 0.0
    for item in test:
        f.write(str(item)+' ')
    f.close()

def wfile(arr):
    f = open('./config.txt','w')
    for item in arr:
        f.write(str(item)+' ')
    f.close()


def psnr1(img1, img2):
   mse = np.mean((img1/1.0 - img2/1.0) ** 2 )
   if mse < 1.0e-10:
      return 100
   return 10 * math.log10(255.0**2/mse)
   
'''   
def psnr2(img1, img2):
   mse = np.mean( (img1/255. - img2/255.) ** 2 )
   if mse < 1.0e-10:
      return 100
   PIXEL_MAX = 1
   return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))'''



















