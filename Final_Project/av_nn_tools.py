#!/usr/bin/env python
#
# ------------------------------------------------------------------------------
# Initialization
# ------------------------------------------------------------------------------
# revision history
#  20200315 (Dr. Bai): baseline train-test software
#  20200315 (Animesh): formatting, commenting, combining both servo and motor
#                      train-test in single method, predict method for making
#                      prediction on single image
#
# usage: from av_nn_tools import NNTools
#
# This script contains required deep learnling tools
#
# ------------------------------------------------------------------------------
# Import Modules
# ------------------------------------------------------------------------------
#
# import global modules
#
import os
import json
import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import torch modules
#
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
from torch.utils.data import DataLoader

# import local modules
#
from av_nn_datagen import Datagen
from raceCarNet import ServoNet, MotorNet

# ------------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------------
TYPE = "servo"
SHAPE = [100, 100]
SETTINGS_FILE = "data/set_servo_train.json"
SEED = 717


# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------

# class: NNTools
#
# This class contains required deep learning tools
#
class NNTools:

    # --------------------------------------------------------------------------
    # method: constructor
    #
    # arguments:
    #  settings: setting file for class parameters
    #
    # return: none
    #
    def __init__(self, settings=SETTINGS_FILE):

        # extract JSON file contents
        with open(settings) as fp:
            content = json.load(fp)

            self.type = content['type']
            self.shape = content['shape']

            self.batch_size = content['batch_size']
            self.epochs = content['epochs']

            self.cuda = content['cuda']
            self.optimizer = content['optimizer']

            clean_start = content['clean_start']
            log_file_path = os.path.join(content['log_dir'], \
                                         content['log_file'])

        # set neural net by type
        torch.manual_seed(SEED)
        if self.type == "servo":
            self.model = ServoNet(self.shape)
        elif self.type == "motor":
            self.model = MotorNet(self.shape)

        # clean start by removing log file
        if os.path.exists(log_file_path) and clean_start:
            os.remove(log_file_path)

        self.datagen_one = Datagen(shape=self.shape)

        return None

    #
    # end of method

    # --------------------------------------------------------------------------
    # method: train
    #
    # arguments:
    #  csvfile: list of images
    #
    # return: none
    #
    # This method runs training session
    #
    def train(self, csvfile):

        # ----------------------------------------------------------------------
        ilist = pd.read_csv(csvfile)["image"].values.tolist()

        # set neural network model
        model = self.model
        if (self.cuda):
            model = self.model.cuda()

        # set loss function
        criterion = nn.MSELoss()
        if (self.cuda):
            criterion = nn.MSELoss().cuda()

        # set optimizer
        optimizer = optim.SGD(model.parameters(), lr=0.0001, momentum=0.9)
        if self.optimizer == 'adam':
            optimizer = optim.Adam(self.model.parameters(), lr=0.0001)
        elif self.optimizer == 'adadelta':
            optimizer = optim.Adadelta(model.parameters(), lr=1.0, \
                                       rho=0.9, eps=1e-06, weight_decay=0)

        # set dataloader
        dataloader = DataLoader(dataset=Datagen(ilist, self.shape), \
                                batch_size=self.batch_size, shuffle=True)

        # ----------------------------------------------------------------------
        total_loss = []
        epoch_loss = 0.0

        # loop over the dataset multiple times
        for epoch in range(self.epochs):

            # initialize train loss and running loss
            batch = 0
            running_loss = 0.0
            start = timeit.default_timer()

            for image, servo, motor in dataloader:

                batch += self.batch_size

                # set input and target
                # implement GPU support if required
                if (self.cuda):
                    input = Variable(image.cuda(non_blocking=True))
                    target = Variable(servo.cuda(non_blocking=True))
                    if self.type == "motor":
                        target = Variable(motor.cuda(non_blocking=True))
                else:
                    input = Variable(image)
                    target = Variable(servo)
                    if self.type == "motor":
                        target = Variable(motor)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward + backward + optimize
                output = model(input)
                loss = criterion(output, target)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()

                # print status for every 100 mini-batches
                if batch % 100 == 0:
                    stop = timeit.default_timer()
                    print('[%3d, %5d] loss: %2.7f time: %2.3f' %
                          (epoch + 1, batch, running_loss / 100, stop - start))

                    epoch_loss = running_loss / 100
                    running_loss = 0.0
                    start = timeit.default_timer()

            total_loss.append(epoch_loss)

        # ----------------------------------------------------------------------
        total_loss = np.array(total_loss)

        # plotting loss vs epoch curve
        plt.figure()
        if self.type == "servo":
            print("servo_dataset training finished!")
            plt.plot(range(epoch + 1), total_loss, linewidth=4)
            plt.title("Servo Data Training")
        elif self.type == "motor":
            print("motor_dataset training finished!")
            plt.plot(range(epoch + 1), total_loss, linewidth=4)
            plt.title("Motor Data Training")

        plt.ylabel("Loss")
        plt.xlabel("Epoch")
        plt.show()
        if self.type == "servo":
            plt.savefig("curves/Loss Curve for Servo Dataset.png")
        if self.type == "motor":
            plt.savefig("curves/Loss Curve for Motor Dataset.png")

        return None

    #
    # end of method

    # --------------------------------------------------------------------------
    # method: test
    #
    # arguments:
    #  csvfile: list of images
    #
    # return: none
    #
    # This method runs training session
    #
    def test(self, csvfile):

        # ----------------------------------------------------------------------
        ilist = pd.read_csv(csvfile)["image"].values.tolist()

        # set neural network model
        model = self.model
        if (self.cuda):
            model = self.model.cuda()

        # set loss function
        criterion = nn.MSELoss()
        if (self.cuda):
            criterion = nn.MSELoss().cuda()

        # set dataloader
        dataloader = DataLoader(dataset=Datagen(ilist, self.shape), \
                                batch_size=self.batch_size, shuffle=True)

        # ----------------------------------------------------------------------

        # initialize train loss and running loss
        batch = 0
        data_count = 0
        running_loss = 0.0
        total_loss = 0.0
        start = timeit.default_timer()

        for image, servo, motor in dataloader:

            batch += self.batch_size
            data_count += self.batch_size

            # set input and target
            # implement GPU support if required
            if (self.cuda):
                input = Variable(image.cuda(non_blocking=True))
                target = Variable(servo.cuda(non_blocking=True))
                if self.type == "motor":
                    target = Variable(motor.cuda(non_blocking=True))
            else:
                input = Variable(image)
                target = Variable(servo)
                if self.type == "motor":
                    target = Variable(motor)

            # forward + loss
            output = model(input)
            loss = criterion(output, target)

            running_loss += loss.item()
            total_loss += loss.item()

            # print status for every 100 mini-batches
            if batch % 100 == 0:
                stop = timeit.default_timer()
                print('[%5d] loss: %2.7f time: %2.3f' %
                      (batch, running_loss / 100, stop - start))

                running_loss = 0.0
                start = timeit.default_timer()

        print('Total accumulated loss = %2.7f' % (total_loss / data_count))
        return None

    #
    # end of method

    # --------------------------------------------------------------------------
    # method: predict
    #
    # arguments:
    #  image: input image
    #
    # return: prediction for single image
    #
    # This method takes an image and predicts servo/motor value from ginen type
    #
    def predict(self, iname):

        image = self.datagen_one.get_image(iname)

        # implement GPU support if required
        model = self.model
        if (self.cuda):
            model = self.model.cuda()
        # return prediction
        if (self.cuda):
            image = Variable(image.cuda(non_blocking=True))
            return model(image).round().int().data.cpu().numpy()[0][0]
        else:
            image = Variable(image)
            return model(image).round().int().data.numpy()[0][0]

    #
    # end of method

    # --------------------------------------------------------------------------
    # method: save_model
    #
    # arguments:
    #  mfile: input model file
    #
    # return: none
    #
    # This method saves a model
    #
    def save_model(self, mfile='models/servo_model.pth'):

        if self.type == "servo":
            print('Saving servo Model ')
            torch.save(self.model.state_dict(), mfile)
        elif self.type == "motor":
            print('Saving motor Model ')
            torch.save(self.model.state_dict(), mfile)

        return None

    #
    # end of method

    # --------------------------------------------------------------------------
    # method: load_model
    #
    # arguments:
    #  mfile: input model file
    #
    # return: none
    #
    # This method loads a model
    #
    def load_model(self, mfile='models/servo_model.pth'):

        # Load model from given file
        self.model.load_state_dict(torch.load(mfile, \
                                              map_location=torch.device('cpu')))

        return None
    #
    # end of method

# ------------------------------------------------------------------------------
# Debugging Block ANI717
# ------------------------------------------------------------------------------
# a = NNTools("data/set_servo_train.json")
# a.train('data/list/list_0.csv')
# a.save_model('models/servo_model.pth')

# aa = NNTools("data/set_servo_test.json")
# aa.load_model('models/servo_model.pth')
# aa.test('data/list/list_2.csv')
# print(aa.predict("data/images/output_0002/i0000000_s15_m15.jpg"))

# b = NNTools("data/set_motor_train.json")
# b.train('data/list/list_0.csv')
# b.save_model('models/motor_model.pth')

# bb = NNTools("data/set_motor_test.json")
# bb.load_model('models/motor_model.pth')
# bb.test('data/list/list_2.csv')
# print(bb.predict("data/images/output_0002/i0000000_s15_m15.jpg"))