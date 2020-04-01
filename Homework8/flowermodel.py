import torch
import torchvision.datasets as datasets
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torchvision.utils import make_grid
from torch.utils.data import random_split
from torch.optim import Adam
from flowernet import FlowerClassifierCNNModel
import torch.nn as nn
from PIL import Image
from util import show_transformed_image


class FlowerModel:
    def __init__(self, data_folder="./data/flowers"):
        self.cnn_model = FlowerClassifierCNNModel()
        self.optimizer = Adam(self.cnn_model.parameters())
        self.loss_fn = nn.CrossEntropyLoss()

        # load data
        self.transformations = transforms.Compose([
            transforms.RandomResizedCrop(64),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

        total_dataset = datasets.ImageFolder(data_folder, transform=self.transformations)
        dataset_loader = DataLoader(dataset=total_dataset, batch_size=100)
        items = iter(dataset_loader)
        image, label = items.next()

        train_size = int(0.8 * len(total_dataset))
        test_size = len(total_dataset) - train_size
        train_dataset, self.test_dataset = random_split(total_dataset, [train_size, test_size])

        self.train_dataset_loader = DataLoader(dataset=train_dataset, batch_size=100)
        self.test_dataset_loader = DataLoader(dataset=self.test_dataset, batch_size=100)

    def train(self, epoches=10):
        for epoch in range(epoches):
            self.cnn_model.train()
            for i, (images, labels) in enumerate(self.train_dataset_loader):
                self.optimizer.zero_grad()
                outputs = self.cnn_model(images)
                loss = self.loss_fn(outputs, labels)
                print("iteration" + str(i) + ":" + str(loss))
                loss.backward()
                self.optimizer.step()

    # My addition - Unsure if this is the correct placement for the method
    def TestAccuracy(self):
        self.cnn_model.eval()
        test_acc_count = 0
        for k, (test_images, test_labels) in enumerate(self.test_dataset_loader):
            test_outputs = self.cnn_model(test_images)
            _, prediction = torch.max(test_outputs.data, 1)
            test_acc_count += torch.sum(prediction == test_labels.data).item()

        test_accuracy = test_acc_count / len(self.test_dataset)
        print("Accuracy percentage: " + str(test_accuracy))

    def predict(self, filename):
        test_image = Image.open(filename)
        test_image_tensor = self.transformations(test_image).float()
        test_image_tensor = test_image_tensor.unsqueeze_(0)
        output = self.cnn_model(test_image_tensor)
        class_index = output.data.numpy().argmax()
        return class_index

    def saveModel(self, modelfile):
        torch.save(self.cnn_model, modelfile)
