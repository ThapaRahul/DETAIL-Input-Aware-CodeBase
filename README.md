# DETAIL-Input-Aware-CodeBase

**Note: Please after the paper is published or put in the archive. Also we need to put bibtex so that if they happen to use our work, they can cite it.**

If you find this work useful, you can cite our paper using:

```
(bibtex)
```

If there are any technical questions after the README, please contact:
* (maybe DETAIL email, if we have one)


## Core Team
* Dependable, Efficient, and Intelligent Computing Lab (DETAIL)
	* Xun Jiao (Faculty)
	* Dongning Ma (Ph.D. Students)
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
6. Run the prunning.py file. 
7. Take note of the error you get from the prunning.
8. Repeat the steps 2-7 for other approximate multipliers.
9. After finishing all the multipliers and moving onto the adders, you need to change the range of first for loop on prunning.py file from range(18-35).
10. Repeat the steps 2-7 for all approximate multipliers.

## Training
**In this section, you need to work with main2.py and Function.py file inside src folder**

### Steps for Training
1. Inside main2.py, set the path variable (around line 14) for the dataset you want to train on.
2. To train the model on a certain quality constraing, make sure to changes the value of quality_const variable (around line 19) to the desired quality. 
3. In out experiment, we use two_point mutation and two_point cross over. However, we also provide functions for three and four point cross over and mutation inside Function.py
4. Inside Function.py file, in the writefile function (around line 328), set the values of the adders and multipliers using the result you got from prunning step. Note, in some units, you have multiple options for approximate adders or multipliers that meet the quality constraint. However, in some units, there is only one value that will meet the constraint. 
5. Make sure the path of str1 in image_print function (around line 270) is to the training image folder.
6. Run the main2.py file.

After the training is complete, you will get final setting in results.txt file inside src folder. It will include the best setting and energy saving informtion. The setting will also be stored as finalSetting.data pickle file.

## Testing
**In this section, you need to work with testing.py and Function.py file inside src folder**

### Steps for Testing
1. Open the testing.py file, and set the path (around line 10) to the image folder you want to test on. 
2. Inside Function.py, in the function image_print (around line 270), change the path of str1 to the image folder you want to test the setting on.
3. Run testing.py and the result will be stored in testResults.txt file. 




