import cv2
import numpy as np
import matplotlib.pylab as plt

#1.	Read the image named “Example1.png”, subtract 50 from all the intensities using for loop, write it with the name imageSub.jpg.
def task1(image):
    copy_image=np.array(image)
    i,j = np.shape(image)
    #print(i,j)
    for k in range(i):
        for l in range(j):
            copy_image[k][l]=image[k][l]-50

    cv2.imshow("image",copy_image)
    cv2.waitKey(-3)


image = cv2.imread("Example1.png")
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#task1(grey_image)

# 2.Read an image, subtract 50 from those regions that have rows and columns in the ranges of 1-50 and 87-133 respectively. Write the image with the name of imageSubSel.jpg.

def task2(image):
    copy_image = np.array(image)
    i, j = np.shape(image)
    # print(i,j)
    for k in range(1,50):
        for l in range(87,133):
            copy_image[k][l] = image[k][l] - 50

    cv2.imshow("image", copy_image)
    cv2.waitKey(-3)

#task2(grey_image)

# 3. Read an image and subtract 50 from those pixels that have intensities greater than 230.
def task3(image):
    copy_image = np.array(image)
    i, j = np.shape(image)
    # print(i,j)
    for k in range(1,50):
        for l in range(87,133):
            if(copy_image[k][l]>230):
                copy_image[k][l] = image[k][l] - 50

    cv2.imshow("image", copy_image)
    cv2.waitKey(-3)

#task3(grey_image)
# 4.Create a function that takes an image as input and produce mirror effect such as shown in figure below

#Histogram Processing

#1.	Write a function named myImHist that is similar to imhist. It should take a grayscale image as input, count the frequencies of each intensity, calculate probability distributive function(pdf), plot pdf vs each intensity and return values of pdf.
def myImHist(image):
    #image1=[[1,2,3],[2,1,3],[1,3,3]]
    min_value = np.min(image)
    max_value = np.max(image)
    j,k = np.shape(image)
    frequency = []
    pdf=[]
    count=0
    total_pixel=0
    for i in range(min_value,max_value+1):
        for a in range(j):
            for b in range(k):
                if image[a][b]==i:
                    print(i)
                    count=count+1
                    print(count)
        frequency.append((i,count))
        total_pixel=total_pixel+count
        count=0
    for intensity , no_of_repeat in frequency:
        pdf.append(no_of_repeat/total_pixel)

    plt.stem(pdf)
    plt.show()
image1 = cv2.imread("download.jpg")
grey_image1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
#myImHist(grey_image1)

# 2. Perform histogram equalization iteratively three times and see if there is any difference in the result or not. Analyze the outcome with the help of some examples.2.	Perform histogram equalization iteratively three times and see if there is any difference in the result or not. Analyze the outcome with the help of some examples.
def Histogram_Equalization(image):
    # image1=[[1,2,3],[2,1,3],[1,3,3]]
    min_value = np.min(image)
    max_value = np.max(image)
    j, k = np.shape(image)
    frequency = []
    pdf = []
    cdf = []
    count = 0
    total_pixel = 0
    sum1=0
    for i in range(min_value, max_value + 1):
        for a in range(j):
            for b in range(k):
                if image[a][b] == i:
                    print(i)
                    count = count + 1
                    print(count)
        frequency.append((i, count))
        total_pixel = total_pixel + count
        count = 0
    for intensity, no_of_repeat in frequency:
        pdf.append(no_of_repeat / total_pixel)
    for value in pdf:
        sum1 = sum1 + value
        cdf.append(sum1)
    plt.stem(cdf)
    plt.show()
image1 = cv2.imread("download.jpg")
grey_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#Histogram_Equalization(grey_image1)

# 3.Find a pre-defined python function that perform histogram matching. Test a few examples for histogram matching using that function.

def predefind_hist_equ(image):
    equ = cv2.equalizeHist(image)
    cv2.imshow("df",equ)
    cv2.waitKey(-1)
image1 = cv2.imread("download.jpg")
grey_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#predefind_hist_equ(grey_image1)

# 4.Create your own function of histogram matching and name it as myHistMatch.

#Spatial and geometric filtering

# 6.Open the Example1.png image as grayscale and display it in the notebook.
#a.	Display histogram of this image (you may use function that was given during the class)
example1 = cv2.imread("Example1.png")
example1_gray = cv2.cvtColor(example1 , cv2.COLOR_BGR2GRAY)
def display_hist(image):
    plt.hist(image)
    plt.show()
#display_hist(example1_gray)
# b.Apply histogarm equlization and display the histagoram of the image and image itself.
def hist_equ(image):
   im= cv2.equalizeHist(image)
   plt.hist(cv2.hconcat([image,im]))
   plt.show()
#hist_equ(example1_gray)

# c.Apply CLAHE histogarm equlization and display the histagoram of the image and image itself. Just use predefined function for that purpose
def Clahe_hist(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl1 = clahe.apply(img)
    plt.hist(cv2.hconcat([img, cl1]))
    plt.show()
#Clahe_hist(example1_gray)

# d.Open the Example1.png image as grayscale and display it in the notebook.d.	Open the Example1.png image as grayscale and display it in the notebook.
def Display_image(img):
    cv2.show(img)
    cv2.waitKey(-1)
#Display_image(example1_gray)