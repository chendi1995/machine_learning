#!/usr/bin/env python
# -*- coding:utf-8 -*-
from numpy import *
import KNN
import matplotlib
import matplotlib.pyplot as plt
datingDataMat,datingLabels=KNN.file2matrix('datingTestSet.txt')
datingDataMat1,ranges,minVals=KNN.autoNorm(datingDataMat)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat1[:,0],datingDataMat1[:,1],15.0*array(datingLabels),15.0*array(datingLabels));
plt.show()
