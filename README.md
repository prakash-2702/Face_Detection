# Face_Detetcion 

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [File Structure](#file-structure)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Contributors](#contributors)
* [Resources](#resources)


<!-- ABOUT THE PROJECT -->
## About The Project 
* Face detection is a computer technology being used in a variety of applications that identifies human faces in digital images.
* OpenCV’s deep learning face detector is based on the Single Shot Detector (SSD) framework with a ResNet base network.
* When using OpenCV’s deep neural network module with Caffe models, you’ll need two sets of files:
  1.The .prototxt file(s) which define the model architecture (i.e., the layers themselves)
  2.The .caffemodel file which contains the weights for the actual layers
  
**Steps followed in this process:**
  1. Constructing the argument parse.
  2. Loading the model files.
  3. Starting the videostream.
  4. Pre-processing of the frames(loading,resizing).
  5. Obtaining the detections and predictions from blob.
  6. Extracting the confidence and filtering the detections.
  7. Showing the required output.

### File Structure
    .
    ├── face_detection.py                          # Driver code
    ├── deploy.prototxt.txt                        # Caffe prototxt files
    ├── res10_300x300_ssd_iter_140000.caffemodel   # Caffe model weight files
    ├── .gitattributes
    └── README.md 
    
<!-- GETTING STARTED -->
## Getting Started

### Prerequisites  
* Python
* OpenCV
* Numpy 
* Imutils
* Argparse

### Installation
1. Clone the repo
```sh
git clone https://github.com/prakash-2702/Face_Detection.git
```    
<!-- CONTRIBUTORS -->
## Contributors
* [Prakash Nadgeri](https://github.com/prakash-2702)
<!-- ACKNOWLEDGEMENTS AND REFERENCES -->
## Resources
* https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* [pyimagesearch](https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/)



