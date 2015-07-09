#!/usr/bin/python
"""
Use a classifier cascade to identify matches in a given image.
"""
import cv2
import cv2.cv as cv
import removematches

def detect(imagefilename):
    '''
    The detect function processes a file to look for matches, and returns a list
    of tuples (x,y) containing the central point of each positive detection.
    '''
    cascade = cv2.CascadeClassifier()
    cascade.load('../data/cascade/wf_cascade.xml')
    img = cv2.imread(imagefilename)
    scalefactor = 0.6 
    if scalefactor!=1:
        width = img.shape[0]
        height = img.shape[1]
        imgscaled = cv2.resize(img,(int(height*scalefactor),int(width*scalefactor)))
    gray = cv2.cvtColor(imgscaled, cv2.COLOR_BGR2GRAY)
    rects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1,
        minSize=(10,10), maxSize=(15,15))
    if len(rects) == 0:
        return []
    matches = []
    for r in rects:
        matches.append((int((1/scalefactor)*(r[0]+r[2]/2)),int((1/scalefactor)*(r[1]+r[3]/2))))
    #return matches
    
    # Filter the matches that we have found in order to get rid of the false positives.
    # This still will not deal with the issue of false negatives, but will increase the precision. 
    filtered_matches = removematches.removematches(img, matches)

    return filtered_matches
    
