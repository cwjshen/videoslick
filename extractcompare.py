import cv2
import datetime
import os
import argparse
import time
from skimage.measure import compare_ssim

start_time = time.time()


parser = argparse.ArgumentParser()
parser.add_argument("-er","--extract_rate", help="time between image extractions in milliseconds, else default 500ms", type=int)
parser.add_argument("-gray","--gray", help="extracts the video in grayscale", action="store_true")
parser.add_argument("video_path", help="relative path to target video for image extraction")
parser.add_argument("gold_img_dir", help="relative path to directory containing golden images")

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
# proceeding to next frame. So to simulate normal playback rate, we do 1000ms / capture fps,
# this gives us no. of ms to wait per frame
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

output_dir = "output/output - %s" % (st)

ret, frame = cap.read()

while(ret):
    try:    
        # Grab millisecond position of current frame
        current_pos = cap.get(cv2.CAP_PROP_POS_MSEC)

        if (current_pos % extract_rate_ms < previous_pos % extract_rate_ms):
          if args.gray:
            cv2.imwrite("output/output - %s/frame%d.jpg" % (st, cap.get(cv2.CAP_PROP_POS_FRAMES)), gray)
            num_frames_extracted += 1
          else: 
            cv2.imwrite("output/output - %s/frame%d.jpg" % (st, cap.get(cv2.CAP_PROP_POS_FRAMES)), frame)
            num_frames_extracted += 1	

        # Current frame will be the previous frame of the next iteration
        previous_pos = cap.get(cv2.CAP_PROP_POS_MSEC)

        ret, frame = cap.read()
    except:
    	print("Number of frames extracted: {0}".format(num_frames_extracted))
    	cap.release()
    	cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()
print("Number of frames extracted: {0}".format(num_frames_extracted))
print("Extraction time: {0} seconds".format(time.time() - start_time))

def compareImages(image_path1, image_path2):
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)
    # Uses scikit's Structural Similarity (SSIM) index implementation
    score, diff = compare_ssim(img1, img2, full=True, multichannel=True)
    return score

pass_count = 0
fail_count = 0

for file_name in os.listdir(output_dir):
    if file_name in os.listdir(args.gold_img_dir):
        result = "FAILED"
        score = compareImages(args.gold_img_dir+'/'+file_name, output_dir+'/'+file_name)
        if score == 1.0:
            result = "PASSED"
            pass_count += 1
        else:
            fail_count += 1
        print('{0} Score: {1} {2}'.format(file_name, score, result))

print("Total Passed: {0}".format(pass_count))
print("Total Failed: {0}".format(fail_count))