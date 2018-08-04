# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 06:49:26 2018

@author: jshka

Code adapted from Hadrien J's blog post explaining Linear Algebra section of
Deep Learning Book

https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.1-Scalars-Vectors-Matrices-and-Tensors/
"""

import numpy as np

##### Vector
#Start by creating a vector, a 1-dimensional array
x = np.array([1, 2, 3, 4])

##### Matrix
#Create a 3x2 matrix
#Array() can create 2-dimensional arrays with nested brackets
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

##### Shape
#Find the shape of the array
A.shape
#Returns (3, 2), telling us the number of rows and columns

#Check the shape of the first vector we created
x.shape
#Returns (4, ), because it has 4 rows and no columns
#This matches the length of the array
len(x) #returns 4

##### Transposition
