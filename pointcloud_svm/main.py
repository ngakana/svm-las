
import laspy
import numpy as np

def read_las(file):
    file = laspy.read(file)
    points = file.xyz

if __name__ == '__main__':
    in_filename = 'jwaneng_highwall_1_labelled_pointcloud.las'
    read_las(in_filename)