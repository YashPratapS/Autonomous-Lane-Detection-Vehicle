# Autonomous-Lane-Detection-Vehicle
The purpose of this project is to create design and develop an autonomous car that can be remotely controlled while also having the ability to detect and avoid obstacles by utilizing Raspberry Pi and Open CV technology. The car is equipped with advanced sensors, which enable it to scan the surrounding environment and detect any potential obstacles. Additionally, the car is also equipped with a camera that captures a live video feed of the road, which is then analyzed by the Open CV library to identify and track lane markings.

![car (1)](https://github.com/YashPratapS/Autonomous-Lane-Detection-Vehicle/assets/95158391/7bc9b0b3-abda-4d1c-9fc6-87fff8a46a22)

# Materials Required::  
- Raspberry Pi (model 3 or higher)
- Pi Camera Module 
- Ultrasonic sensor (HC-SR04) 
- L298N motor driver 
- 3 DC Motors 
- Power bank 
- Chassis (3-wheel drive)

![image](https://github.com/YashPratapS/Autonomous-Lane-Detection-Vehicle/assets/95158391/cdf56f15-e041-4a41-aa47-eb49016530cb)

After completing the assembly and connection parts we will be implementing various functionalities to our model which is divided into three parts of which operating the car remotely (Using a Computer) is first – We have used MobaXterm which is remote computing software and it allowed us to access the Raspbian operating system using IP address of the Raspberry Pi for wireless connectivity. We want to control the movement of the car using our computer i.e. the motion will be determined by the keys we press on the keyboard. So for that, we have made three Python files namely - motors.py, keyboard.py, and testdrive.py.

- Keyboard.py :
We want to read the impression from the keyboard as specific keys are assigned for specified motions. We have imported the Pygame [7] library to our code as it provides an easy-to-use interface to work with graphics, sound, and input devices such as keyboards and mice and helps to read the input that is provided from the keyboard. Our function repeatedly checks if a key is pressed or not and returns the assigned key as a result in the output. For example if ‘W’ is pressed then the output will depict W and so on.
- Motors.py :
After the key impression is received from the keyboard.py function, the next step is carried out by motors.py. We imported the GPIO library to our code as it will allow us to easily access the GPIO pins of a Raspberry Pi board. Now the GPIO pins are initialized for connection to the L298N motor module and raspberry pi. Now the servo motors of the car can be controlled using raspberry pi. We make a new file with the name motor.py for the movement of the car. Now when a command from the keyboard is passed to the motor.py file a function call will take place i.e. if W is pressed it is assigned to the forward motion function, S is assigned for backward motion, A  for steering the servo motors to the left and D for steering the servo motor to the right. The autonomous car is equipped with three servo motors, with two located at the front for controlling the forward and steering movements, and one at the back for controlling the backward movement and enabling the car to turn left or right.
- Test.py :
The last step is to command the car for motion and for that; we have made a new file named test.py. Here we have first imported keyboard.py and motors.py files. Now simply in this file, the output from the keyboard.py and motors.py files will be sensed and the required commands will follow. If W is pressed the car will move in the forward direction. If S is pressed the car will move in the backward direction. If A is pressed the car will steer in the left direction. If D is pressed the car will steer in the right direction hence we can simply operate our Vehicle with the computer.
