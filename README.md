# RaspPiGroup3
Dr. Bai's Raspberry Pi Class Group 3
### To Run

```bash
git clone https://github.com/Bigkid325/RaspPiGroup3

# launch teleop joy node
cd teleop_ws
source ./devel/setup.bash
cd src/teleop_twist_joy/launch
roslaunch teleop.launch

#in another terminal:
cd teleop_ws
source ./devel/setup.bash
rosrun teleop_twist_joy testservont.py

```
