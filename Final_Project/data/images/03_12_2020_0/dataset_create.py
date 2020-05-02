import os
from shutil import copy
import pandas as pd


data = pd.read_csv("../Resources/03_12_2020/output_15.csv")

path = "data/images/03_12_2020/output_0015/"
if not os.path.exists(path):
    os.makedirs(path)

root = "../Resources/03_12_2020/images/output_15/"
dest = "data/images/03_12_2020/output_0015/"

#for i,image in enumerate(os.listdir("../Resources/03_10_2020/images/output_0/")):
#    print(image)
    
for index in range(len(data)):
    image = data["image"][index].split("/")[-1]
    
    servo = int(float(data["servo"][index])*100)
    motor = int(float(data["motor"][index])*100)
    
    src = root + image
    dst = 'i{:07d}_s{:02d}_m{:02d}.jpg'.format(index, servo, motor)
    dst = dest + dst
#    print(dst)
    copy(src,dst)