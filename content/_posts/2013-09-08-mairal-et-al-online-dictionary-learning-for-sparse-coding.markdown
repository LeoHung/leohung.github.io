---
layout: post
title: "Mairal et al. Online dictionary learning for sparse coding"
date: 2013-09-08 00:35
comments: true
categories: ammai 
---

Mairal et al. Online dictionary learning for sparse coding. ICML 2009.	

The following figures are all from this paper. 

The paper goal is to propose a online learning method to learn sparse coding dictionary, the basis set which can represent specific data through linear combination, for large scale data. 

## Algorithm

{% img center /images/ammai/03/online_learning_algorithm.png %}

The algorithm is showed above. Assuming the training set composed of i.i.d. samples of a distribution, the method is minimizing the cost function, the difference between linear combination of basis set and real data, by stochastic gradient discent to find decomposing coefficient $latex \alpha $ and dictionary $latex D$ iteratively. 

{% img center /images/ammai/03/online_updating_algorithm.png %}

Their algorithm above for updating the dictionary uses block-coordinate descent. 

## My comment

The work is solid because they present not only the experiment result  but also the sophisticated theoretical proof showing the convergence of the online learning method; however, the assumption, the training set composed of i.i.d. samples of a distribution, may be suspicious because it is not alway satisfied in real world.	
