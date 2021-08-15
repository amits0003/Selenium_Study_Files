import cv2 as cv
import numpy

for index in list(dir(cv)):
    print(index)

with open('res.txt' , 'w+') as fileptr:
    fileptr.writelines(dir(cv))
