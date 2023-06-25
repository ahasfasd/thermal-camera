# 热成像使用教程
## 解压
将文件解压到~/catkin_ws/src 文件夹下
## 环境及配置
python 2.7 ROS默认
确保环境已经安装opencv-python和numpy
```
pip install opencv-python
```
```
pip install numpy
```
## 步骤
cd ~/catkin_ws
catkin_make
source devel/setup.bash
roslaunch facthem receive.launch
rviz

打开rviz添加image，将话题选为/web_cam/image_raw
## 注意事项
请务必将scripts的rece.py文件内的人脸识别库的路径改为绝对路径
若报错 ，请查询rece.py是否为可执行文件，或者检查摄像头是否已经正确连接
