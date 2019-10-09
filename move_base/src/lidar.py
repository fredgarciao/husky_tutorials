#!/usr/bin/env python
import rospy
import numpy
#from std_msgs import *
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class laser():

    def __init__(self):
        
        
        self.velocity_publisher = rospy.Publisher('/cmd_vel',
                                                    Twist, queue_size=10)
        self._laser = rospy.Subscriber("/scan", LaserScan, self.callback)


        self.velx = 5   
        self.vely = 5
     
    #def callback (self, msg):
    #    self.laser_msg = msg.ranges
    #    print (len(self.laser_msg))
    #    rospy.spin()
    def velo (self):
        self.velocity_publisher.x = self.velx
        self.velocity_publisher.y = self.vely

        


if __name__ == "__main__":
    rospy.init_node('lasertest', anonymous=True)
    
    la = laser()
    while not rospy.is_shutdown():
        la.velo()
