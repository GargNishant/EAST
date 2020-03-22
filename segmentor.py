import cv2
import os
import numpy as np

min_x = 0
min_y = 0
max_y = None
max_x = None
sorted_line_words = {}

""" 
This method is responsible for pre-processing the boxes passed and calling methods to save the sorted coord's
for a single Image

@param output_dir: Complete Output Directory
@param input_image: Complete path to image to be processed. Including name of the image
@param all_boxes: All Boxes predicted by the model. These are not pre-processed 
"""
def save_image_coords(input_image,output_dir, all_boxes):
	
    global min_y, min_x, max_x, max_y, line_words

    if all_boxes is None:
        print("No Text Recognized")
        return
    
    #res_file = os.path.join(output_dir,'{}.txt'.format(os.path.basename(input_image).split('.')[0]))
    image_boxes = []
    image = cv2.imread(input_image)[:, :, ::-1]
    for box in all_boxes:
        # to avoid submitting errors
        box = sort_poly(box.astype(np.int32))
        if np.linalg.norm(box[0] - box[1]) < 5 or np.linalg.norm(box[3]-box[0]) < 5:
            continue
        cv2.polylines(image[:, :, ::-1], [box.astype(np.int32).reshape((-1, 1, 2))], True, color=(255, 255, 0), thickness=1)
        image_boxes.append([box[0, 0], box[0, 1], box[1, 0], box[1, 1], box[2, 0], box[2, 1], box[3, 0], box[3, 1]])
    max_y, max_x, ch = image.shape
    min_x = 0
    min_y = 0
    line_number = 0
    
    sorted_word_count = 0
    while sorted_word_count < len(image_boxes):
        top_left_word = find_top_left_word(image_boxes)
        line_words = find_line_words(image_boxes,top_left_word)
        sorted_words = sort_words(line_words)
        sorted_word_count += len(sorted_words)
        sorted_line_words[line_number] = sorted_words
        min_y = top_left_word[7]
        line_number += 1
        
    sorted_boxes = []
    for i in range(line_number):
        list_ = sorted_line_words[i]
        for box in list_:
            sorted_boxes.append(box)

    return sorted_boxes


def sort_poly(p):
    min_axis = np.argmin(np.sum(p, axis=1))
    p = p[[min_axis, (min_axis+1)%4, (min_axis+2)%4, (min_axis+3)%4]]
    if abs(p[0, 0] - p[1, 0]) > abs(p[0, 1] - p[1, 1]):
        return p
    else:
        return p[[0, 3, 2, 1]]


"""
This method is used to find the top left word between the contraints.
@param image_boxes: A list which contains a List of 8 points denoting a single Rectangle

@return: List of 8 points representing Coordinates of the Top Left Word in given constraints
"""
def find_top_left_word(image_boxes):
	global min_y, min_x, max_x, max_y
	curr_y = max_y
	top_words = []
	for box in image_boxes:
		if box[1] < curr_y and box[1] > min_y:
			top_words = []
			curr_y = box[1]
			top_words.append(box)
		elif box[1] == curr_y:
			top_words.append(box)

	curr_x = max_x
	top_left_word = None
	for box in top_words:
		if box[0] < curr_x:
			curr_x = box[0]
			top_left_word = box

	return top_left_word

"""
Finds all the words which are some-what aligned to the top_left_word
@param image_boxes: List of All boxes predicted by model
@param top_left_word of the line

@return: A list of all the words aligned with top_left_word
"""
def find_line_words(image_boxes,top_left_word):
	line_words = []
	for box in image_boxes:
		if box[1] >= top_left_word[1] and box[1] <= top_left_word[7]:
			line_words.append(box)
	return line_words


"""
This is used to sort the values using the merge sorting algorithm, in-place
@param nlist: List of integers that we want to sort
"""
def mergeSort(nlist):
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1

"""
Sorts the words from a given list of words, based on x-coordinate in Ascending order
@param line_words: List of words which are supposed to exist in 1 line

@return: List of Sorted boxes from the given list
"""
def sort_words(line_words):
    sorted_words = []
    x_values = []
    x_value_dict = {}
    for i in range(len(line_words)):
        x = ((line_words[i])[0])
        x_values.append(x)
        x_value_dict[x] = (line_words[i])

    mergeSort(x_values)
    for x in x_values:
    	sorted_words.append(x_value_dict[x])
    return sorted_words