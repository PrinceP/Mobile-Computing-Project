"# Mobile-Computing-Project" 

#1: Convert the given video to frames 

frame_generation.py
usage \n

      python frame_generation.py --input sample_vid.mp4 --output sample_frame --frames .1

It will create a folder of given output, based on the frame per sec argument. Default fps is 1.
Needed software - ffmpeg
https://www.ffmpeg.org/

#2: Images blur removals

image_blur.py

usage

    python image_blur.py --images Frames --threshold 1000


	--images      Folder containing frames
	--threshold   Can be varied,Default value is set to 100

Tutorial 
  http://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/

In Progress 

#3: Watershed algorithm 
usage
	
	python groundplane_detection.py

Tutorial 
  http://docs.opencv.org/3.1.0/d3/db4/tutorial_py_watershed.html

