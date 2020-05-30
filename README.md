# DETAIL-Input-Aware-CodeBase

**Note: Please update this part with a short description of the work and link to the paper after the paper is published or put in the archive. Also we need to put bibtex so that if they happen to use our work, they can cite it.**

If you find this work useful, you can cite our paper using:

```
(bibtex)
```

If there are any technical questions after the README, please contact:
* connectthapa84@gmail.com


## Core Team
* Dependable, Efficient, and Intelligent Computing Lab (DETAIL)
	* Xun Jiao (Faculty)
	* Dongning Ma (Ph.D. Students)
	* Wanli Chang (Ph.D. Students)
	* Rahul Thapa (Undergraduate Student)
	* Xingjian Wang (Undergraduate Student)


## Table of Contents
1. [Requirements](#requirements) to install on your system
2. How to use [dataset](#dataset)
3. How to use [prunning](#prunning)
4. Steps for [training](#training)
5. Steps for [testing](#testing)

## Requirements

The main requirements are listed below:
* Python 3.6
* Numpy
* OpenCV 4.2.0

## Dataset

The dataset we used in out experiment consists of cat-vs-dog dataset and butterfly dataset. The link to these datasets are given below

* Cat-vs-Dog: https://www.kaggle.com/c/dogs-vs-cats/data
* Butterfly: http://www.josiahwang.com/dataset/leedsbutterfly/

We have also provited a imgs_data folder with 40 images each of cats, dogs, and butterfly images separated. If you want to use it, please copy and paste the entire imgs_data folder inside the main project file, for example (SobelFilter-master2-5.0/imgs_data) 

**For the ease of our user, we have created 3 folders for conducting experiments on three different applications: Sobel, Laplacian, and Prewitt. The code has an absolute path in some locations. Please modify the path according to you folder path.**

## Prunning
**In this section, you need to work with prunning.py file and Function.py file. Both of these files can be found at the src folder of given application. For example, SobelFilter-master2-5.0/src/prunning.py**

### Steps for Prunning
1. Inside prunning.py file, set a path (line 7) to the dataset you intend to train on.
2. The first for loop goes through adders and multipliers. Remember, for the number of adders and multipliers are different for different applications. For Sobel and Prewitt, the first 18 units are multipliers and rest 17 are adders. For Laplacian, the first 9 units are multipliers and rest 7 are adders. 
3. First, change the for loop for range(0, 18) to go through the multipliers. 
4. Now, go to Function.py file and and on image_print function (around line 270), change the str1 variable file path to the image folder you intend to train on.
5. Inside the same file, go to function writefile_t and change the value of test[i] to the lowest approximation multiplier. 
6. Run the prunning file. 
7. Take note of the error you get from the prunning.
8. Repeat the steps 2-7 for other approximate multipliers and adders. Remember, after finishing all the multipliers and moving onto the multiplier, you need to change the range of firs for loop on prunning.py file from range(18-35).

## Training


## Testing




