---
layout: post
title: "Support vector learning for ordinal regression"
date: 2013-09-07 23:43
comments: true
categories: ammai
---
"Support vector learning for ordinal regression," R. Herbrich, T. Graepel, K. Obermayer, ICANN, 1999

Authors: R. Herbrich, T. Graepel, K. Obermayer 
The following figures are all copies from the paper.

The classical supervised machine learning methods deal with classification problem and regression problem. Instead, this research proposed a method to deal with ordinal regression, predicting the order of samples, by reducing ordinal regression problem into a classification problem on pair of object. 

Assume input space X ={x1, x2,...xk }, and output space  Y = {y1, y2 ...yk} where exist a order that y1 &lt; y2 &lt; y3 ... &lt; yk. The ordinal regression problem is to find a model h mapping from X to Y such that minimize the loss function, which panelize wrong order mappings. 

To transfer it into classification problem, define a function p = p( h(x_1), h(x_2) ) ={-1, 0 ,+1} which means the classes of order: &lt; , = , or &gt;. Then, the classification problem can be transformed to find a model h that mapping from (h(x_1), h(x_2) ) to ( y_1, y_2) to minimize the loss function which is related to whether p(h(x_1),h(x_2)) is as same as p(y_1,y_2). 

After transformation, it can be solved by support vector machine. The experiment compared ordinal regression with multi-class SVM and support vector regression(SVR). The result showed that ordinal regression is better than others. 

{% img center /images/ammai/05/r_measure.png %}

Furthermore, the research experimented on a IR problem, and it shows that ordinal regression performed better. 

{% img center /images/ammai/05/IR_result.png %}

## My Opinion

According to the authors said, these work introduced a new problem in machine learning filed, and they proposed a novel and simple method to deal with ordinal regression problem. However, due to reducing process using combination of instance, I think that it will become become a big problem when the dataset grossing. When the number of instance gross  to n, the number of combination gross to O(n^2), which is hard to compute if n is large.	