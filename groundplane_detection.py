import cv2
import numpy as np
from imutils import paths
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="image file name")
ap.add_argument("-o", "--out", required=True,help="output image file name")
args = vars(ap.parse_args())


img = cv2.imread(args['image'],1)
orig_img = img.copy()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

sure_bg = cv2.dilate(opening,kernel,iterations=3)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

(row,col) =  markers.shape
cut_rows = []

for col1 in range(1,col-2):
	for row1 in range(row-2, 1, -1):
		if markers[row1,col1] == -1:
			cut_rows.append(row1)
			break

cut = min(cut_rows)
crop_img = orig_img[cut:row,0:col]
crop_mark = markers[cut:row,0:col]
(row2,col2) = crop_mark.shape

for c in range(1,col2):
	for r in range(0,row2):
		if crop_mark[r,c] != -1:
			crop_img[r,c] = [0,0,0]
		elif crop_mark[r,c] == -1:
			break


#cv2.imshow('image',img)
#cv2.imshow('image1',crop_img)
cv2.imwrite(args['out']+'.png', crop_img)
cv2.waitKey(0)
