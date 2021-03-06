
https://github.com/Bigkid325/RaspPiGroup3/tree/master/Final_Project

## Train Your model

```bash 
git clone https://github.com/Bigkid325/RaspPiGroup3

cd Final_Project

#trains data
python raceCarModel.py

#Test Accuracy
python rcCarAcuracy.py
```
####  Accuracy output 
![image](https://raw.githubusercontent.com/Bigkid325/RaspPiGroup3/master/Final_Project/Screenshots/DeepinScreenshot_select-area_20200430203508.png)

#### Total accumulated loss
![image](https://raw.githubusercontent.com/Bigkid325/RaspPiGroup3/master/Final_Project/Screenshots/DeepinScreenshot_select-area_20200502130939.png)

## Copy files to your Raspberry Pi

#### On your Raspberry Pi
```bash
git clone git clone https://github.com/Bigkid325/RaspPiGroup3
```
Copy your trained model from your computer to the Raspberry Pi and place it in
the models folder. This can be done using scp or rsync on the command line or another tool.

#### Install torch and Torchvision

```
wget https://github.com/lbaitemple/ubuntu_server_rpi/raw/master/torch/torch-1.6.0a0%2B521910e-cp36-cp36m-linux_armv7l.whl
wget https://github.com/lbaitemple/ubuntu_server_rpi/raw/master/torch/torchvision-0.7.0a0%2Bfed843d-cp36-cp36m-linux_armv7l.whl

pip3 install [path to those two files]
```
#### Test Prediction Speed on Raspberry Pi
```bash
python test.py
```

### Prediction Speed Output
![image](https://raw.githubusercontent.com/Bigkid325/RaspPiGroup3/master/Final_Project/Screenshots/DeepinScreenshot_select-area_20200430203414.png)

Speed = 0.07
