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
    #change range of array to (0-10)
    self.arr = self.arr*10
    #add number 4 
    self.arr = np.append(self.arr,4)
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
    newline = dataSorter(numb=20)
    newline.sortArray()
    arr=newline.sortArr
    arr1 = arr.tolist()
   
def binary_search4(arr1,target_val):
  lower=0
  upper=len(arr1)-1
  while lower<=upper: #make sure there is still value in the list
    mid=(lower+upper)//2 #start with the middle position
    if arr1[mid]==target_val: #get the position of target value
      return mid 

    elif arr1[mid]<target_val: 
      lower=mid+1 # narrow the search region
    else:
      upper=mid-1  # arr1[mid] > target_val narrow the search region
  else:
    return None
print(arr)
print("The postion of 4 is: ",binary_search4(arr1,4))
    
