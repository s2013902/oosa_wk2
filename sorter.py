'''
A class to build on 
and produce a binary
search algorithm
'''
import matplotlib.pyplot as plt
import numpy as np
from sys import exit

#####################################

class dataSorter(object):
  '''A class to hold data and provide examples of search algorithms'''

  def __init__(self,numb=100):
    '''Class initialiser'''
    self.numb=numb
    self.arr=np.random.random((numb))

  def sortArray(self):
    '''Sort an array, using a simple sort method'''
    # preserve original array by copying
    copArr=np.copy(self.arr)
    # create workspace
    self.sortArr=np.empty(self.arr.shape)
    # sort the array
    for i in range(0,copArr.shape[0]):
      minN,minInd=self.findMin(copArr)
      self.sortArr[i]=minN
      copArr[minInd]=1000000

  def findMin(self,arr):
     minN=10000  # a big number
     minInd=0
     for i in range(0,arr.shape[0]):
       if(arr[i]<minN):
         minN=arr[i]
         minInd=i
     return(minN,minInd)
  
if __name__=='__main__':
    #Get 20 random sorted number for x coordinate 
    newline=dataSorter(numb=20)
    newline.sortArray()
    newsort=newline.sortArr
    print(newsort)
    
