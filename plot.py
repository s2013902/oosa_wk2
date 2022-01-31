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

    #'''Find a minimum, needed for soret'''
    #print("Could not complete function. Needs finishing.")
    #print(" Exiting program now")
    #exit

    
if __name__=='__main__':
    #Get 20 random sorted number for x coordinate 
    xcoor=dataSorter(numb=20)
    xcoor.sortArray()
    x=xcoor.sortArr

    #Get 20 random sorted number for y coordinate
    ycoor=dataSorter(numb=20)
    ycoor.sortArray()
    y=ycoor.sortArr

    #set the labels
    plt.xlabel('x')
    plt.ylabel('y')
    #plot with a line
    plt.plot(x,y)
    plt.show()


    #name a file
    filename="sorted_array_line.png"

    #write the graph to a file
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x,y)
    plt.savefig(filename) 
    #close the file
    plt.close()
    #clear everything to start a new plot
    plt.clf()

    plt.xlabel('x')
    plt.ylabel('y')
    #plot with a point
    plt.plot(x,y,'.')
    plt.plot(x,y)
    plt.show()
   
    #name a file
    filename="sorted_array_point.png"

    #write the graph to a file
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x,y,".")
    plt.savefig(filename) 
    #close the file
    plt.close()
    #clear everything to start a new plot
    plt.clf()
    
