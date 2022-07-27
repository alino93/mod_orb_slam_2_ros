#!/usr/bin/env python
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import glob

class Nodo(object):
	def __init__(self):
		self.image = None
        	self.bridge = CvBridge()
		self.rate = rospy.Rate(10) # 10hz
		self.pub = rospy.Publisher('/camera/image_raw', Image,queue_size=10)
		self.filenames = glob.glob("/media/alino/3365-3132/dataset2/images/*.png")
		self.filenames.sort()
		#self.images = [cv2.imread(img) for img in self.filenames]
		rospy.loginfo('Image address received!')

	def publisher(self):
		for name in self.filenames:
			if rospy.is_shutdown():
				break
			rospy.loginfo("Published image!")
			img = cv2.imread(name)
			self.pub.publish(self.bridge.cv2_to_imgmsg(img))
			self.rate.sleep()
    
if __name__ == '__main__':
	rospy.init_node('read_img')
	my_node = Nodo()
	my_node.publisher()



