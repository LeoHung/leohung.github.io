---
layout: post
title: "Semi-Supervised Hashing for Scalable Image Retrieval"
date: 2013-09-08 00:40
comments: true
categories: ammai
---
J\. Wang et al, "Semi-Supervised Hashing for Scalable Image Retrieval," CVPR, 2010.

The following figures and formula are all copied from this paper.

## Novelty

Unsupervised learning method, like LSH, would ignore the relationship of labels; however, supervised learning method modified from LSH, like RBM or SH, would cost time to compute and require much training data to avoid overfitting. To coping with these problems, the authors introduce a semi-supervised learning method: SSH.

## Technical Summarization

SSH(Semi-Supervised Hashing) is based on two idea: (1) distribute the similar label images to the closer hash (2) make each hash bucket balanced. Assume that $latex M $ is the images pairs set in which have same label, and $latex C $ is the images pairs set where have different labels. The following objective function is main to the first criterion: for pairs with same label, maximize the probability such that they have fall into the closer buckets; for pairs with different, minimize such probability.

![03different](/images/ammai/03/different.png)

Besides, they add a regularization to constraint such that each bucket size should be balanced: hash functions should be orthogonal.

![balance_constraint](/images/ammai/03/balance_constraint.png)

Nevertheless, the balancing constraints are hard, so it is replaced by a "soft" constraint, instead of requiring orthogonality, maximizing the variance of mapping space.

<p style="text-align: center;">$latex \sum_k{E[ { \left \| h_k(x) - \mu \right \|}^{2} ]}$</p>

The following figure is the comparison between state-of-the-art methods and SSH in large scale data. They demonstrate that SSH with no-orthogonal performs better than other algorithms

![w4_result](/images/ammai/03/w4_result.png)

## My comments

Just as the authors claim, SSH can maintain the semantic meanings consistency, unlike LSH method, and do not require too much time like supervised learning methods like RBM and SH. Due to SSH is a semi-supervised method, SSH must have label data to train model; however, in reality, the labels are often missing or incomplete. I am curious how to conquer this problem, which is not the main point solved by the study, but I think it is important because it will occur in practice.