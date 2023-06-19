##热成像摄像头使用方法


首先下载官方ros对应的usb_cam，使用命令```sudo apt install ros-<versions>-usb-cam


切换到usb_cam所在的路径下，路径在/opt/ros/noetic/share/usb_cam/launch, 打开usb_cam-test.launch, 将文件中的image_width和image_height分别改为256和192


下载颜色转换包ir_convert, 下载后进入文件夹将文件中CMakeLists的set OpenCV_DIR 改为你自己opencv头文件所在的目录


编译ir_convert, 使用catkin_make 进行编译,编译完成后记得source一下


##文件启动


1 ```roslaunch usb_cam usb_cam-test.launch```


2 ```roslaunch ir_convert ir_convert.launch```
