# Racecar Project Homework 6
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
```
### To have subscriber and publisher on same machine
```bash
cd src/teleop_twist_joy/launch
roslaunch teleop.launch

#in another terminal:
cd RaspPiGroup3/teleop_ws
source ./devel/setup.bash


#controller.py is the file the controls the car
rosrun teleop_twist_joy controller.py

#testservont.py is the subscriber code
rosrun teleop_twist_joy testservont.py
```
### To have subscriber and publisher on different machine
```bash
#On Machine A (publisher / controller)
#First clone repo and follow directions above
#run:
 export ROS_MASTER_URI=http://{ip_of_machine_A}:11311
 export ROS_IP={ip_of_machine_A}
 roslaunch teleop.launch
 rosrun teleop_twist_joy controller.py

#On machine B (the subscriber / robot)
#First clone repo and follow directions above
#run:
 export ROS_MASTER_URI=http://{ip_of_machine_A}:11311
 export ROS_IP={ip_of_machine_B}
 rosrun teleop_twist_joy testservont.py
 
 ```
### Sample output csv located in ~/teleop_ws/out.csv
A csv file is automatically created and starts saving data as soon as the program starts. It is saved as out.csv
Click [here](https://github.com/Bigkid325/RaspPiGroup3/blob/master/teleop_ws/out.csv) to go to sample csv file
