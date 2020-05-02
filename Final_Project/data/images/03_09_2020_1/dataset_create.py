#!/usr/bin/env python
#
#------------------------------------------------------------------------------
# Initialization
#------------------------------------------------------------------------------
# revision history
#  20200306 (Animesh): baseline software
#  20200310 (Animesh): modified file path and names for proposed format
#
# usage: python rc_csv_to_image
#
# This script extracts image, servo and motor data from CSV file
#
#------------------------------------------------------------------------------
# Import Modules
#------------------------------------------------------------------------------
#
# import global modules
#
import os
import cv2
import numpy as np
import pandas as pd
import matplotlib

#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------
CSV_IMG_FILE = '../Resources/03_09_2020__/output_0044.csv'
BASE_ODIR_IMG = 'data/images/'
BASE_ODR_ANNO = 'data/annotations/'

WIDTH = 148
HEIGHT = 102
DEPTH = 3

#------------------------------------------------------------------------------
# Main Method
#------------------------------------------------------------------------------
# method: main
#
# arguments: none
#
# return: none
#
# This method is the main function
#
def main():

    width = WIDTH
    height = HEIGHT
    depth = DEPTH

    # extract CSV file contents
    data = pd.read_csv(CSV_IMG_FILE)

    # extract file name 'output_002'
    fname = CSV_IMG_FILE.split('.')[-2].split('/')[-1]

    # define image directory name
    img_dir_name = BASE_ODIR_IMG + \
        CSV_IMG_FILE.split('.')[-2].split('/')[-2] + '/' + fname + '/'

    # create image directory if it doesn't exist
    if not os.path.exists(img_dir_name):
        os.makedirs(img_dir_name)

    for index in range(len(data)):

        # extract image data as numpy array
        car_img = data['image'][index]
        car_img = np.fromstring(car_img[1:-1], sep=', ', dtype='uint8')
        car_img = np.resize(car_img, (height, width, depth))

        # extract servo and motor data
        servo = int(round(data['servo'][index]*100))
        motor = int(round(data['motor'][index]*100))

        # create image name
        name = 'i{:07d}_s{:02d}_m{:02d}.jpg'.format(index, servo, motor)

        # save image 
        matplotlib.image.imsave(img_dir_name + name, \
                                cv2.cvtColor(car_img, cv2.COLOR_RGB2BGR))

#------------------------------------------------------------------------------
# Driver Program
#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

#                                                                            
# end of file
# ANI717