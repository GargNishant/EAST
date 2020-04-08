# EAST_OCR: An OCR solution using Neural Networks and Classic OCR solution 
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


### TODO:
- [x] Push my Commits to GitHub
- [x] Update Readme for working of the Solution 
- [ ] Include a Demo Colab File
- [ ] Include Photos in GitHub Readme
