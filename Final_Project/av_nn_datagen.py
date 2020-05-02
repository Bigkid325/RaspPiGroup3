#!/usr/bin/env python
#
#------------------------------------------------------------------------------
# Initialization
#------------------------------------------------------------------------------
# revision history
#  20200315 (Animesh): baseline software
#
# usage: from av_nn_datagen import Datagen
#
# This script generates data for neural network training session
#
#------------------------------------------------------------------------------
# Import Modules
#------------------------------------------------------------------------------
#
# import global modules
#
import cv2

# import torch modules
#
import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms

# import local modules
#
from av_parse_data import ParseData

#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------
SHAPE = [100,100]

#------------------------------------------------------------------------------
# Classes
#------------------------------------------------------------------------------

# class: Datagen
#
# This class generates data for neural network training session
#
class Datagen(Dataset):

    #--------------------------------------------------------------------------
    # method: constructor
    #
    # arguments:
    #  dfile: 
    #
    # return: none
    #
    def __init__(self, ilist=None, shape=SHAPE):
        
        self.transform = transforms.Compose([transforms.ToTensor()])
        
        self.ilist = ilist
        self.shape = shape
        
        self.parsedata = ParseData()

        return None
    #
    # end of method
    
    #--------------------------------------------------------------------------
    # method: get_image
    #
    # arguments:
    #  ifile: input image file
    #
    # return:
    #  image: image tensor
    #
    # This method returns image tensor
    #
    def get_image(self, ifile):
        
        image = self.parsedata.parse_image(ifile)
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)
        image = self.transform(image)
        return image.unsqueeze(0)
    #
    # end of method

    #--------------------------------------------------------------------------
    # method: getitem
    #
    # arguments: 
    #  index: index for list of images
    #
    # return: image, servo, motor
    #
    # This method returns data
    #
    def __getitem__(self, index):
        
        # parse image, servo and motor data
        image,servo,motor = self.parsedata.parse_data(self.ilist[index])
        
        # convert image, servo and motor data to tensor
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)
        image = self.transform(image)
        servo = torch.tensor(float(servo))
        motor = torch.tensor(float(motor))
        
        return image, servo, motor
    #
    # end of method

    #--------------------------------------------------------------------------
    # method: length
    #
    # arguments: none
    #
    # return: none
    #
    # This method returns length of data
    #
    def __len__(self):
        
        return len(self.ilist)
    #
    # end of method







#------------------------------------------------------------------------------
# Debugging Block ANI717
#------------------------------------------------------------------------------
#from torch.utils.data import DataLoader
#
#file = 'data/list/list_1.csv'
#
#dataloader = DataLoader(dataset=Datagen(file,shape=[10,8]), batch_size=1000, \
#                        shuffle=True)
#for image, servo, motor in dataloader:
#    print(image.shape)
#    print(servo, motor)