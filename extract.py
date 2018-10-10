import cv2
import datetime
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-er","--extract_rate", help="time between image extractions in milliseconds, else default 500ms", type=int)
parser.add_argument("-gray","--gray", help="extracts the video in grayscale", action="store_true")
parser.add_argument("video_path", help="relative path to target video for image extraction")
args = parser.parse_args()

# Grab current time stamp and create directory to contain extracted frames
st = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# Create output directories to store extracted images
if not os.path.exists("output"):
	os.mkdir("output")
os.mkdir("output/output - %s" % st)

# Create VideoCapture object
cap = cv2.VideoCapture(args.video_path)

# Using cv2.waitKey for playback, which defines how long in milliseconds to wait before 
# 	proceeding to next frame. So to simulate normal playback rate, we do 1000ms / capture fps,
#		this gives us no. of ms to wait per frame
normal_playback_msperframe = int(1000/cap.get(cv2.CAP_PROP_FPS))

# Rate at which we extract frames in ms, obtained as command line arg or default to 500ms
if args.extract_rate:
	extract_rate_ms = args.extract_rate
else:
	extract_rate_ms = 500

num_frames_extracted = 0

# Variables to track frame position in milliseconds using cap_prop_pos_msec
current_pos = 0
previous_pos = 0

while(cap.isOpened()):
  try:
    ret, frame = cap.read()

    # Grab millisecond position of current frame
    current_pos = cap.get(cv2.CAP_PROP_POS_MSEC)
    # print(current_pos % extract_rate_ms, previous_pos % extract_rate_ms)
    
    if args.gray:
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	cv2.imshow('Video', gray)
    else:
    	cv2.imshow('Video', frame)

    # Quits playback 'q' keypress
    if cv2.waitKey(normal_playback_msperframe) & 0xFF == ord('q'):
			print("Number of frames extracted: {0}".format(num_frames_extracted))
			cap.release()
			cv2.destroyAllWindows()
			break

		# We want to write every 500 ms, but the frame positions might not line up exactly with 500ms
		#		so we'll grab the first frame that comes immediately after every 500ms interval.
		#		The position of every current frame % extract_rate should always be greater than the 
		#		the the previous position except for when we pass the extract_rate interval of 500ms. 
		#		Ex: current frame @ 1503ms and previous frame @ 1497 -> 1503 % 500 < 1497 % 500 
    if (current_pos % extract_rate_ms < previous_pos % extract_rate_ms):
    	if args.gray:
    		cv2.imwrite("output/output - %s/frame%d.jpg" % (st, cap.get(cv2.CAP_PROP_POS_FRAMES)), gray)
    		num_frames_extracted += 1
    	else: 
    		cv2.imwrite("output/output - %s/frame%d.jpg" % (st, cap.get(cv2.CAP_PROP_POS_FRAMES)), frame)
    		num_frames_extracted += 1	


    # Current frame will be the previous frame of the next iteration
    previous_pos = cap.get(cv2.CAP_PROP_POS_MSEC)
  except:
		print("Number of frames extracted: {0}".format(num_frames_extracted))
		cap.release()
		cv2.destroyAllWindows()

