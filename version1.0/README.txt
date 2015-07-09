REQUIRED LIBRARIES: 

OpenCV 2.4.10 
lxml 3.4.0(included in core Python package on Unix-based OS, needs to be installed separately for Windows)




EVALUATING A WHITEFLY DETECTOR:

To run an example whitefly detection with a standard object detection method (Haar classifier cascade), 
run the findaccuracy.py script in the src directory.


cd src/
findaccuracy.py (calculates performance statistics with no image display)

findaccuracy.py --show  (displays each test image, with detected whiteflies and ground truth)


When displaying images, press escape to quit or any other key to advance to the next test image.




CREATING A NEW WHITEFLY DETECTOR:

Create a new module with a detect() function, for example by copying cascadedetect.py. 
This function, given an image filename as input, should return a list of (x,y) tuples containing the image coordinates of detected whiteflies. 
Then reference this module from findaccuracy.py, by changing references of cascadedetect to [name of new module].


Note that the cascade detector has many false positives. 
So one idea might be to take the cascade detector output and apply some further filtering based perhaps on color or contour information. 
Many other approaches may work though...