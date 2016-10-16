import cv2
from imutils import paths
import argparse
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="video file name with path")
ap.add_argument("-o", "--output", required=True,
	help="video file name with path")
ap.add_argument("-t", "--frames", type=float, default=1.0,
	help="frames per second")
args = vars(ap.parse_args())


x = os.getcwd()
directory = x + '/' + args['output']

if not os.path.exists(directory):
    os.makedirs(directory)


os.system('ffmpeg -i '+args['input']+' -vf fps='+str(args['frames'])+'  '+args['output']+'/images%05d.png')