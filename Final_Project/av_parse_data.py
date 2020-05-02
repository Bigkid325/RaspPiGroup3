#!/usr/bin/env python
#
#------------------------------------------------------------------------------
# Initialization
#------------------------------------------------------------------------------
# revision history
#  20200313 (Animesh): baseline software
#
# usage: from av_parse_data import ParseData
#
# This script parses image, servo and motor data
#
#------------------------------------------------------------------------------
# Import Modules
#------------------------------------------------------------------------------
#
# import global modules
#
import cv2

#------------------------------------------------------------------------------
# Classes
#------------------------------------------------------------------------------

# class: ParseData
#
# This class parses datas
#
class ParseData:

    #--------------------------------------------------------------------------
    # method: constructor
    #
    # arguments: none
    #
    # return: none
    #
    def __init__(self):

        return None
    #
    # end of method

    #--------------------------------------------------------------------------
    # method: parse_data
    #
    # arguments:
    #  fname: file name
    #
    # return: image data, servo data, motor data
    #
    # This method parses image, servo and motor data from given image file
    #
    def parse_data(self, fname):
        
        return self.parse_image(fname), \
                    self.parse_servo(fname), self.parse_motor(fname)
    #
    # end of method
    
    #--------------------------------------------------------------------------
    # method: parse_image
    #
    # arguments:
    #  fname: file name
    #
    # return: image data
    #
    # This method parses image data from given image file
    #
    def parse_image(self, fname):

        return cv2.imread(fname)
    #
    # end of method
    
    #--------------------------------------------------------------------------
    # method: parse_servo
    #
    # arguments:
    #  fname: file name
    #
    # return: servo data
    #
    # This method parses servo data from given image file
    #
    def parse_servo(self, fname):
        
        return int(fname.split('/')[-1].split('.')[0].split('_')[-2][1:3])
    #
    # end of method
    
    #--------------------------------------------------------------------------
    # method: parse_motor
    #
    # arguments:
    #  fname: file name
    #
    # return: motor data
    #
    # This method parses motor data from given image file
    #
    def parse_motor(self, fname):
        
        return int(fname.split('/')[-1].split('.')[0].split('_')[-1][1:3])
    #
    # end of method







#------------------------------------------------------------------------------
# Debugging Block ANI717
#------------------------------------------------------------------------------
#a = CarUtility()
#img, servo, motor = a.parse_data('data/images/output_0002/i0000009_s15_m16.jpg')