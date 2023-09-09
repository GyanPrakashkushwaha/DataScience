# RCNN

## 1. Introduction
The CNN based object detection techniques have improved dramatically over the last few years. The journey starts with R-CNN followed by Fast R-CNN, Faster R-CNN, mask R-CNN, and YOLO. These are all very simple, very intuitive, and easy to implement algorithms. Personally, I have found them very fascinating. I intend to write medium stories for all of them……

R-CNN is the first in the family. Understanding R-CNN is crucial as it will lay the foundation to understand subsequent algorithms.

## 2. First Look at RCNN

![Image](https://miro.medium.com/v2/resize:fit:828/format:webp/1*lW4453vRf1gERyRotAAQZQ.jpeg)

- The regions that are extracted from an input image are called region proposals.
- RCNN extracts only around 2000 region proposals from an input image. (All 2000 images will not actually contain objects of our interest)
- As the CNN can only accept inputs with a fixed size, all the extracted region proposals are first converted to a fixed size of 227 x 227 pixels. This is called image warping.
- These fixed-size region proposals are then fed to a Large convolutional neural network consisting of five convolutional layers and two fully connected layers to get a fixed-length features vector for each region proposal.
- These feature maps are then passed to a set of linear SVMs to predict the actual objects in corresponding region proposals. The number of SVMs is equal to the number of classes in the dataset plus 1.
- For example, if the dataset contains 200 classes, then 201 linear SVMs are used in the last stage. 1 extra class is for background. The background of the image is treated as one class.
- Thus each SVM corresponds to one class. So each class-specific SVM will predict if the region proposal contains the corresponding object or not.
- After that, a bounding box regressor uses a linear regression model to predict more accurate bounding boxes in terms of location.

The above steps are summarized in Figure 5 below.

![Image](https://miro.medium.com/v2/resize:fit:720/format:webp/0*JjAXZCJJR0n8TOnk.png)

## 3. More Insights into R-CNN

According to Wikipedia:

Given an input image, R-CNN begins by applying a mechanism called Selective Search to extract regions of interest (ROI), where each ROI is a rectangle that may represent the boundary of an object in the image. Depending on the scenario, there may be as many as two thousand ROIs. After that, each ROI is fed through a neural network to produce output features. For each ROI’s output features, a collection of support-vector machine classifiers is used to determine what type of object (if any) is contained within the ROI.

Ross Girshick et al. introduced R-CNN in November 2013. Object detection has come a long way since then. The more recent algorithms are based on foundations laid by R-CNN. Hence it is crucial for aspiring computer vision engineers to understand R-CNN.

### 3.1 How Region Proposals are Generated?

As a very first step of R-CNN, we have to generate region proposals from an image, which can then be warped and fed to CNN for further processing. R-CNN is agnostic to region proposal methods. Which means we can use any method to generate region proposals. The authors of R-CNN have used Selective Search. The corresponding research paper by J.R.R. Uijlings et. al. gives the details of selective search.

![Image](https://miro.medium.com/v2/resize:fit:828/format:webp/1*Yh_zicid04eOpJWJn-VtSg.jpeg)

The criterion used to differentiate a region proposal from the rest of the image is worth giving a thought.

- Image (c) in Figure 6 contains a chameleon whose color is matching a lot with its surrounding. So we have to use a criterion of texture to differentiate and extract chameleon from the rest of the image.
- Image (b) in Figure 6 contains two cats whose texture is the same. So we have to use a criterion of color.
- In image (d), the wheel of the car has different color and texture from the car, and we may, by mistake, declare it as a separate region. Images are intrinsically hierarchical. Hence wheels and the rest of the car should merge into one object.
- On the contrary, in image (a), the spoon is inside the bowl, and the bowl stands on the table. But we may want to declare spoon and bowl as separate objects instead of merging them into the table and declaring them as one object.

The bottom-line here is, there do not exist a single strategy for generating region proposals.

Selective search algorithm presents a variety of diversification strategies to deal with as many image conditions as possible.

![Image](https://miro.medium.com/v2/resize:fit:828/format:webp/1*FgmQHR6CoLgNubUAle9MLw.jpeg)

The process of selective search can be explained in the following steps with the help of Figure.

- A set of small starting regions which ideally do not span multiple objects is created as shown in the first column of Figure 7.
- Similarities between all the adjacent regions are found and two most similar regions are grouped together.
- Again similarities are found and grouping is done. This process is repeated as shown in Figure 7.

Three types of diversification strategies are used.

- Variety of color spaces with increasing degree of invariance in terms of light intensity, shadow/shading, highlights.
- By using different similarity measures like color similarity, texture similarity, encouraging small regions to merge early and measuring how well two regions fit into each other.
- Varying the complimentary starting regions.

Around 2000 region proposals thus created are warped and fed to CNN as shown in Figure.

### 3.2 The Need of Bounding Box Regressor

This is a refinement step. A bounding box given by selective search is represented using [x, y, w, h], where x, y are the coordinates of the top-left corner of the region proposal and w, h are width and height of the region proposal. This bounding box given by selective search is further refined by bounding box regressor. Here, A linear regression model is trained to predict a modified window. This way localization error is further reduced and mAP is improved by 3 to 4 points.

### 3.3 Training and Evaluation of R-CNN

R-CNN is trained on ILSVRC2013 dataset. ILSVRC stands for ImageNet Large Scale Visual Recognition Challenge. The dataset is split into train (395918 images), val (20121 images) and test (40152 images) sets.

Three types of training occur in R-CNN. 1) CNN fine-tuning 2) SVM training 3) bounding box regressor training.

At test time, we again obtain 2K region proposals for every image, warp them, feed them to CNN, get their score from SVMs, and then R-CNN uses something called as NMS (Non-maximum suppression) to reject unwanted region proposals. An object may have been detected by more than one region proposal. NMS will consider only those proposals that have higher SVM score than its learned threshold. NMS will also reject a region if it has overlap (IoU) with another region having a higher SVM score. This way we get the best region proposal for a given object.

### 3.4 Results

![Image](https://miro.medium.com/v2/resize:fit:828/format:webp/1*BZozuKSIBSwV3ArnciEFVw.png)

Figure shows mAP comparison with various other techniques present prior to R-CNN. Note that methods preceded by * in Figure use outside training data in the test set. BB stands for bounding box. As it is very clear from figure that R-CNN outperformed all other techniques on ILSVRC2013 dataset.

### 3.5 Drawbacks of R-CNN

- It takes more than 40 seconds to detect the objects in a test image which makes it unsuitable for real-time applications.
- The CNN has to run for every region proposal. There is no weight sharing.

## Paper
[Link](https://arxiv.org/pdf/1311.2524.pdf)
