# An OCR solution using Neural Networks and Classic OCR solution 
### Introduction:
This is an OCR Solution, which uses the Modern Neural Network for Word Detection and Classical OCR techniques to Read the text from any image file. The complete solution works in 2 Stages:
1. Detection of individual words from an Image.
2. Passing the detected words to OCR Engine to identify the characters in the word

### Word Detection:
+We first detect the Bounding Boxes around the Words, using the Deep Learning Model [EAST: An Efficient and Accurate Scene Text Detector](https://arxiv.org/abs/1704.03155v2).
+ Using the Bounding Boxes, individual Words are also saved as seperate Words. The words are saved in the Order of Top-to-Bottom, Right-to-Left.

### OCR Engine:
+Using one of the most famous OCR engine Tesseract, the characters are recognized from the individual Words from the Word Detection method.
+The individual characters are appended to a txt file which is saved after the characters are recognized from all the individally detected words

### Pre-Trained Model
1. Models trained on ICDAR 2013 (training set) + ICDAR 2015 (training set): [BaiduYun link](http://pan.baidu.com/s/1jHWDrYQ) [GoogleDrive](https://drive.google.com/open?id=0B3APw5BZJ67ETHNPaU9xUkVoV0U)
2. Resnet V1 50 provided by tensorflow slim: [slim resnet v1 50](http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz)

### TODO:
- [x] Push my Commits to GitHub
- [x] Update Readme for working of the Solution

### Credits:
1. Original Implementation of [EAST Detector](https://github.com/argman/EAST)
2. [PyTesseract](https://pypi.org/project/pytesseract/)
