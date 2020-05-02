#!/usr/bin/env python
#
# ------------------------------------------------------------------------------
# Initialization
# ------------------------------------------------------------------------------
# revision history
#  20200315 (Dr. Bai): baseline train-test software
#  20200315 (Animesh): formatting, commenting, modified to make compatioble
#                      with any shape of image input
#
# usage: from racecarNet import ServoNet, MotorNet
#
# This script contains required deep learnling models
#
# ------------------------------------------------------------------------------
# Import Modules
# ------------------------------------------------------------------------------
#
# import global modules
#
import numpy as np

# import torch modules
#
import torch
from torch.nn import Module
from torch.nn import Conv2d, Linear
from torch.nn.functional import elu
import torch.nn.functional as F
import torch.nn as nn
from torch.autograd import Variable
# ------------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------------
SHAPE = [100, 100]  # [shape_y,shape_x]


def get_flat_fts(in_size, fts):
    f = fts(torch.autograd.Variable(torch.ones(1, *in_size)))
    return int(np.prod(f.size()[1:]))
# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------

# class: ServoNet
#
# This class contains deep learning model for servo data prediction
#
class ServoNet(Module):

    # --------------------------------------------------------------------------
    # method: constructor
    #
    # arguments:
    #  shape: input image shape
    #
    # return: none
    #

    def __init__(self, shape):
        super(ServoNet, self).__init__()

        self.input_size = [3, shape[0], shape[1]]
        self.features = nn.Sequential(
            Conv2d(3, 6, 3, stride=(2, 2)),
            Conv2d(6, 12, 3, stride=(2, 2)),
            Conv2d(12, 10, 3)
  
        )

        self.flat_fts = get_flat_fts(self.input_size, self.features)
        self.classifier = nn.Sequential(
            nn.Linear(self.flat_fts, 10),
            nn.Linear(10, 1),
        )

        return None

    #
    # end of method

    # --------------------------------------------------------------------------
    # method: forward
    #
    # arguments:
    #  x: image tensor
    #
    # return:
    #  x: output tensor
    #
    # This method passes tensors through neural network model
    #
    def forward(self, x):
        fts = self.features(x)
        flat_fts = fts.view(-1, self.flat_fts)
        out = self.classifier(flat_fts)
        return out

    #
    #
    # end of method
    # generate input sample and forward to get shape

# ------------------------------------------------------------------------------
# class: MotorNet
#
# This class contains deep learning model for motor data prediction
#
class MotorNet(Module):

    # --------------------------------------------------------------------------
    # method: constructor
    #
    # arguments:
    #  shape: input image shape
    #
    # return: none
    #
    def __init__(self, shape):
        super(MotorNet, self).__init__()
        self.flatsize = int(10 * (np.ceil((np.ceil((shape[0] - 2) / 2) - 2) / 2) - 6) * \
                            (np.ceil((np.ceil((shape[1] - 2) / 2) - 2) / 2) - 6))

        self.conv1 = Conv2d(3, 24, 3, stride=(2, 2))
        self.conv2 = Conv2d(24, 36, 3, stride=(2, 2))
        self.conv3 = Conv2d(36, 48, 3)
        self.conv4 = Conv2d(48, 64, 3)
        self.conv5 = Conv2d(64, 10, 3)
        self.fc1 = Linear(self.flatsize, 10)
        self.fc2 = Linear(10, 1)

        return None

    #
    # end of method

    # --------------------------------------------------------------------------
    # method: forward
    #
    # arguments:
    #  x: image tensor
    #
    # return:
    #  x: output tensor
    #
    # This method passes tensors through neural network model
    #
    def forward(self, x):
        x = elu(self.conv1(x))
        x = elu(self.conv2(x))
        x = elu(self.conv3(x))
        x = elu(self.conv4(x))
        x = elu(self.conv5(x))
        x = x.view(-1, self.flatsize)
        x = elu(self.fc1(x))
        x = elu(self.fc2(x))

        return x
    #
    # end of method