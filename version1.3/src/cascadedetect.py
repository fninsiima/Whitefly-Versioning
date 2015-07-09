#!/usr/bin/python
"""
Use a classifier cascade to identify matches in a given image.
"""
import cv2
#import cv2.cv as cv

def detect(img):
    '''
    The detect function processes a file to look for matches, and returns a list
    of tuples (x,y) containing the central point of each positive detection.
    '''
    cascade = cv2.CascadeClassifier()
    cascade.load('../data/cascade/wf_cascade.xml')
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(10,10), maxSize=(25,25))
    matches = []
    
    for r in rects:
        xcentre = r[0] + r[2] / 2
        ycentre = r[1] + r[3] / 2
        matches.append((xcentre,ycentre))
    
    return matches;
        
    #filtered_matches = removematches.removematches(img, matches)
    #after removing false positives
    #return filtered_matches


 
