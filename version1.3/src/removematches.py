'''
Created on Nov 13, 2011

@author: David Lluncor
@author: Ethan Liang
@author: Madieh 

This file describes our approach given a matching coordinates
from the cascade detector, we are trying to remove false positives.

Our main approach has been to try to focus on a small bounding box around the
matched coordinate. We define a few features that determine whether this
matching point we have found is valid.

Does it have enough white pixels?
Does it have a light green background?
Is it a light color overall, aka not soil?
'''
import cv2

WIDTH = 15 # Width of box we are investigatng per matched point.
HEIGHT = 15 # Height of box we are investigating per matched point.

def removematches(img, matches):
    """
    Entrance point into this module. 
    @param imagefilename The filepath of the image to analyze.
    @param matches The list of matching coordindates passed to us by some classifier.
    """
    
    img_hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

    filtermatches = []
                  
    for match in matches:
        if isPatchOK(img, img_hsv, match):
            filtermatches.append(match)
            
    return filtermatches
    
def isPatchOK(img, img_hsv, match):
    """
    @return True if the coordinate should be considered a true positive.
    """
    
    #match is a tuple (x, y)
    (avghue, avgsat, avgval, whiteratio) = find_features(img, img_hsv, match[0], match[1], WIDTH, HEIGHT)
        
    #Make sure the color is approximately green by considering the green hue space.
    is_background_light_green = avghue > 35 and avghue < 75
    is_saturation_approximately_white = avgsat < 50
    are_there_too_little_white_points = whiteratio < 0.0001
    
    if are_there_too_little_white_points:
        return False
    
    if is_background_light_green: 
        return True
    else:
        #Don't get rid of too many of the white colors, make sure 
        # Low saturation means lighter color
        # High value more of a white color
        if is_saturation_approximately_white:
            return True
        
    return False
    
def find_features (img, img_hsv, x, y, w, h):
    """ 
    Return relevant pieces of information about a small window around
     a particular pixel.
     Looking at the window in HSV format.
     
     @return averagehue average hue value for the window.
     @return averageval average val for the window. 
     @return averagesat average saturation for the window.
     @return whiteratio ratio of white pixels in the window.
    """
        
    # Define the coordinates for the window around the point to analyze
    leftx = max(0, x - w//2) #top left x coordinate of box  
    topy = max(0, y- h//2) #top right y coordinate of box
    rightx = min(leftx+w, img.shape[1]-1)
    bottomy = min(topy+h, img.shape[0]-1)
    #rect = cv.getSubRect(img_hsv, (topleftx, toplefty, width, height))
    rect = img_hsv[topy:bottomy,leftx:rightx,:]
    
    # Calculate features for that box.
    sumh = 0
    sumv = 0
    sums = 0
    numwhite = 0.0
    for i in range(rect.shape[0]):
        for j in range(rect.shape[1]):
            sumh += rect[i, j][0] #hue
            sums += rect[i, j][1] #saturation
            sumv += rect[i, j][2] #val
            
            is_white_pixel = rect[i, j][2] > 150
            if (is_white_pixel):
                numwhite = numwhite + 1
                
    numpixels = rect.shape[0] * rect.shape[1]
    
    whiteratio = numwhite / (numpixels)
    averagehue = sumh / (numpixels)
    averagesat = sums / (numpixels)
    averageval = sumv / (numpixels)
    
    return (averagehue, averagesat, averageval, whiteratio)    
