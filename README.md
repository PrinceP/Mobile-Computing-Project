"# Mobile-Computing-Project" 

#1: Convert the given video to frames 

frame_generation.py
usage

      python frame_generation.py --input sample_vid.mp4 --output sample_frame --frames .1
      
      --input full path to video
      --output folder where frames will be stored
      --frames fps in float format only.

It will create a folder of given output, based on the frame per sec argument. Default fps is 1.

Required - ffmpeg
https://www.ffmpeg.org/

#2: Removal of blurred images

image_blur.py

usage

    python image_blur.py --images Frames --threshold 1000


	--images      Folder containing frames
	--threshold   Can be varied,Default value is set to 100

Tutorial 
  http://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/


#3: Ground plane detection
usage
	
	python groundplane_detection.py --image GroundPlane/images00495.png

Tutorial 
  http://docs.opencv.org/3.1.0/d3/db4/tutorial_py_watershed.html

![alt tag](https://raw.githubusercontent.com/PrinceP/Mobile-Computing-Project/master/images00495.png)
![alt tag](https://raw.githubusercontent.com/PrinceP/Mobile-Computing-Project/master/GP1.png)

#4: Superpixels 
usage
      
      python super_pixel.py --image GroundPlane/images00495.png --pixels 400


      --image image file
      --pixels number of segments

Tutorial

http://www.pyimagesearch.com/2014/07/28/a-slic-superpixel-tutorial-using-python/

![alt tag](https://raw.githubusercontent.com/PrinceP/Mobile-Computing-Project/master/images00495.png)
![alt tag](https://raw.githubusercontent.com/PrinceP/Mobile-Computing-Project/master/superpixels_400_segments.png)

