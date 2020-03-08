# RaspPiGroup3
Dr. Bai's Raspberry Pi Class Group 3
### To Run

```bash
git clone https://github.com/Bigkid325/RaspPiGroup3

# launch teleop joy node
cd RaspPiGroup3/teleop_ws
sudo rm -r build/ devel/
catkin_make
source ./devel/setup.bash
cd src/teleop_twist_joy/launch
roslaunch teleop.launch

#in another terminal:
cd RaspPiGroup3/teleop_ws
source ./devel/setup.bash

#in third terminal:
cd RaspPiGroup3
mkdir ~/bagfiles
cd ~/bagfiles
rosbag record -a

#run bag2csv.py file in third terminal after accumulating data in bag file
python bag2csv.py

#testservont.py is the file the controls the car
rosrun teleop_twist_joy testservont.py

```
