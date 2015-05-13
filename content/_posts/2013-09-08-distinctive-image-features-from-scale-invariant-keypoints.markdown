---
layout: post
title: "Distinctive Image Features from Scale-Invariant Keypoints"
date: 2013-09-08 00:07
comments: true
categories: ammai
---

"Distinctive Image Features from Scale-Invariant Keypoints," Lowe, IJCV, 2004	

<a href="http://mslab.csie.ntu.edu.tw/~askus/ammai/blog/wp-content/uploads/2012/03/螢幕快照-2012-03-13-下午11.11.08.png"> </a>

Paper author: David G. Lowe The following figures are all from this paper. 

## Novelties, contributions, assumption 

This work introduce a set of promising affine invariant features, which can be used to identified specific object varied with background, illumination, rotation degree. 

## Questions and promising applications

Object Recognition by keypoints matching. 

## Technical Summarization

Scale Invariant Feature Transform (SIFT) contains two main part: finding keypoints and describing them. The process contains four steps: 

### Step 1
Scale-space extrema detection To find keypoints, the first thing is to detect scale-space extrema points, where are significant different from their neighbors. Koenderink (1984) and Lindeberg (1994) showed that the only possible scale-space kernel is the Gaussian function. Using the Gaussian function convolution on the image with varying scales, calculate the difference from the nearby two scales separated ny a constant factor k for finding the points whose difference is local maximum or minimum. 

{% img center /images/ammai/03/螢幕快照-2012-03-13-下午8.32.36.png %}

{% img center /images/ammai/03/螢幕快照-2012-03-13-下午8.34.58.png %}

Two reasons support this method: (a) it is a particularly efficient function to compute (b) In addition, the difference-of-Gaussian function provides a close approximation to the scale-normalized Laplacian of Gaussian, σ2∇2G, as studied by Lindeberg (1994)

### Step 2. Keypoint localization 

{% img center /images/ammai/03/螢幕快照-2012-03-13-下午8.40.52.png %}
 
In order to detect the local maxima and minima of D(x, y, σ), each sample point is compared to its eight neighbors in the current image and nine neighbors in the scale above and below (see Figure 2)Three problem left: a. k=? b. σ=? c. How many octaves?After finding keypoints, the next problem is to accurate the keypoint localization and eliminate edge responses.

### Step 3 Orientation assignment 

{% img center /images/ammai/03/螢幕快照-2012-03-13-下午10.43.34.png %}

Calculate the magnitude and the orientation of the gradient of keypoints. To make the descriptor is invariant to rotation, the orientation can be represented relative to the the dominant direction.</li> 

### Step 4 Keypoint descriptor 

{% img center /images/ammai/03/螢幕快照-2012-03-13-下午11.11.08.png %}

To describe the sample point, use m x m pixels within n x n blocks surrounding the point with k orientation bins. Sum up the orientations of m x m pixels to k bins weighted by magnitudes for each block. Therefore, one sample point would have n * n * k dimensions features vector to represent.The vector is normalized to unit length for the purpose that let the descriptor is invariant to the effects of illumination change, such as contrast, causing pixels value  multiplied with a constant factor.Besides, a non-linear illumination changes may be caused by 3D surfaces with differing orientations or  camera saturation. To cope with it, reduce the inﬂuence of large gradient magnitudes by thresholding the values in the unit feature vector to each be no larger than 0.2, and then renormalizing to unit length