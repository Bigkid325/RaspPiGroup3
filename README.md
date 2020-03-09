# RaspPiGroup3
Dr. Bai's Raspberry Pi Class Group 3
### To Run

```bash
#link https://github.com/Bigkid325/RaspPiGroup3/tree/master
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


#controller.py is the file the controls the car
rosrun teleop_twist_joy controller.py

#testservont.py is the subscriber code

```
