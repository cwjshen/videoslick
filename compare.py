import cv2
import argparse
import os
from skimage.measure import compare_ssim

parser = argparse.ArgumentParser()
parser.add_argument("gold_img_dir", help="relative path to directory containing golden images")
parser.add_argument("test_img_dir", help="relative path to directory containing images to be validated")
args = parser.parse_args()

def compareImages(image_path1, image_path2):
	img1 = cv2.imread(image_path1)
	img2 = cv2.imread(image_path2)
	# Uses scikit's Structural Similarity (SSIM) index implementation
	score, diff = compare_ssim(img1, img2, full=True, multichannel=True)
	return score

for file_name in os.listdir(args.test_img_dir):
	if file_name in os.listdir(args.gold_img_dir):
		score = compareImages(args.gold_img_dir+'/'+file_name, args.test_img_dir+'/'+file_name)
		print('{0} Score: {1}'.format(file_name, score))