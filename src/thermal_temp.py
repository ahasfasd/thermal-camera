#!/usr/bin/python3
# coding:utf-8

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import time 
import os
import numpy as np
from std_msgs.msg import Header

path=os.path.abspath("/home/hy/catkin_ws/src/ir_convert/config/haarcascade_frontalface_default.xml")
classfier = cv2.CascadeClassifier(path)


# Initialize the cv_bridge object
bridge = CvBridge()





# Define the image callback function
def image_callback(msg):
    try:
        # Convert the ROS image to OpenCV format
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)

    # Perform some image processing on the cv_image here
    
#    while not rospy.is_shutdown():  # Ctrl C正常退出，如果异常退出会报错device busy！
    
    start = time.time()
        #ret, frame = capture.read()
        
    if cv_image.size!=0:  
        color = (255, 255, 0)
            #frame = frame[0:191, 0:191, 0]
            #color_img = cv2.applyColorMap(frame, cv2.COLORMAP_SPRING)
        faceRects = classfier.detectMultiScale(cv_image, scaleFactor=1.1, minNeighbors=3, minSize=(32, 32))
        num = 0
        font = cv2.FONT_HERSHEY_SIMPLEX
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect

                num += 1
                if num > 1000:
                    break
                temp_g = 0
                for xx in range(x, x + w):
                    for yy in range(y, y + h):
                        
                        
                        temp_g = temp_g + (cv_image[xx, yy])[0]
                temp_tem = temp_g / (w * h)
                temp = temp_tem*36.5/130
               
                cv2.rectangle(cv_image, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                
                    # 图片，标注文字，左上角坐标，字体形式，字体大小，颜色，字体粗细
                cv2.putText(cv_image, 'T:%.1f' % (temp), (x + 30, y + 30), font, 1, (255, 255, 0), 4)
        cv2.drawMarker(cv_image,position=(128,81),color=(255, 255, 0),markerSize =10, markerType=cv2.MARKER_CROSS, thickness=1)
        temp_middle = (cv_image[128,80])[0]
        temp_middle = temp_middle*36.5/130
        cv2.putText(cv_image, '%.1f' %(temp_middle),(130,80),font,1,(255,255,0),4)
        ros_frame = Image()
        header = Header(stamp=rospy.Time.now())
        header.frame_id = "Camera"
        ros_frame.header = header
        ros_frame.width = 256
        ros_frame.height = 384
        ros_frame.encoding = "bgr8"
        ros_frame.step = 1920
            #ros_frame.data = np.array(color_img).tostring()  # 图片格式转换
            #cv2.imshow("aaa", ros_frame.data)
            #print(type(ros_frame))
            #image_pub.publish(ros_frame)  # 发布消息
        end = time.time()
        #print("cost time:", end - start)  # 看一下每一帧的执行时间，从而确定合适的rate
        rate = rospy.Rate(25)  # 10hz
    
    
    

    try:
        # Convert the OpenCV image back to ROS format
        processed_msg = bridge.cv2_to_imgmsg(cv_image, "bgr8")
        processed_msg.header = msg.header
        # Publish the processed image to a new topic
        pub.publish(processed_msg)
    except CvBridgeError as e:
        print(e)

if __name__=='__main__':
    # Initialize the ROS node and create a subscriber and publisher
    rospy.init_node('image_processor')
    sub = rospy.Subscriber('/usb_cam/image_raw', Image, image_callback)
    pub = rospy.Publisher('/processed_image', Image, queue_size=10)

    # Spin the node to listen for incoming messages
    rospy.spin()
