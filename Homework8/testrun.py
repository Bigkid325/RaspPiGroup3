from flowermodel import FlowerModel
import torch

a = FlowerModel()
a.train()
#a.saveModel(modelfile="flower.pth") # need to search code to save the model
torch.save(a, "flower.pth")
a.TestAccuracy()
indx=a.predict(filename="./data/flowers/daisy/5547758_eea9edfd54_n.jpg")
print(indx)

model = torch.load("flower.pth")
model.TestAccuracy()