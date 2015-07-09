REQUIRED LIBRARIES: 
OpenCV 2.4.10 
lxml 3.4.0 (included in core Python package on Unix-based OS, needs to be installed separately for Windows)




EVALUATING A WHITEFLY DETECTOR:
To run an example whitefly detection with a standard object detection method (Haar classifier cascade), 
run the findaccuracy.py script in the src directory.


cd src/
findaccuracy.py (calculates performance statistics with no image display)

findaccuracy.py --show  (displays each test image, with detected whiteflies and ground truth)


When displaying images, press escape to quit or any other key to advance to the next test image.



CHANGES: Takes the cascade detector output and applies some further filtering based on color to decrease the number of false positives. 