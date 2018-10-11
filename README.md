# VideoSlick
Image extraction and comparison from videos

## Getting Started

### Prerequisites / Libraries Used

This project assumes installation of Python and uses the following third party libraries

* OpenCV - https://opencv.org/
* scikit-image - http://scikit-image.org/docs/dev/api/skimage.html

The OpenCV .pyd file is included in the repository and scikit-image comes included in most Python distributions like Anaconda.

### Clone Repository
```
git clone https://github.com/cwjshen/videoslick.git
```

### Overview of Directories and Files

* [extract.py](https://github.com/cwjshen/videoslick/blob/master/extract.py) - Script that extracts individual image frames from a given video
* [compare.py](https://github.com/cwjshen/videoslick/blob/master/compare.py) - Script that compares images using skimage's implementation of Structural Similarity Index
* [videos](https://github.com/cwjshen/videoslick/tree/master/videos) - Directory containing videos to be processed
* [golden images](https://github.com/cwjshen/videoslick/tree/master/golden%20images) - Directory containing golden images by video
* [test images](https://github.com/cwjshen/videoslick/tree/master/test%20images) - Directory containing grayscaled images by video to compare against golden images.
* output - After running extract.py, an output folder will be generated that will store the extracted images and be marked with a timestamp

The image files are extracted and named as "frame{#}" where # corresponds to the frame position in the video from which it was extracted from.

### Running the scripts

#### extract.py
* extract.py takes one required argument that is the relative path to the target video for image extraction
```
python extract.py 'videos/testvideo.mp4'
```
* extract.py also takes some optional arguments:
  * `[-h, --help]` - Displays help menu for running the script
     ```
     python extract.py -h
     ```
  * `[-er EXTRACT_RATE, --extract_rate EXTRACT_RATE]` - Time between image extractions in milliseconds. Defaults to 500ms if not provided.
     ``` 
     python extract.py 'videos/testvideo.mp4' -er 2000 
     ```
   * `[-gray, --gray]` -  Extracts the images in grayscale, used to generate test images
     ```
     python extract.py 'videos/testvideo.mp4' -gray
     ```
     ```
     python extract.py 'videos/testvideo.mp4' -er 2000 -gray
     ```
     
#### compare.py
* compare.py takes two required arguments that are:
  * `[gold_img_dir]` - Relative path to directory containing golden images
  * `[test_img_dir]` - Relative path to directory containing images to be validated
  ```
  python compare.py 'golden images/testvideo' 'test images/testvideo'
  ```
#### extractcompare.py

Single script that extracts images from a given video file then compares them with given golden images and outputs a summary of test results

* compare.py takes two required arguments that are:
  * `[video path]` - Relative path to directory containing golden images
  * `[test_img_dir]` - Relative path to directory containing images to be validated
* extract.py also takes some optional arguments:
  * `[-h, --help]` - Displays help menu for running the script

  * `[-er EXTRACT_RATE, --extract_rate EXTRACT_RATE]` - Time between image extractions in milliseconds. Defaults to 500ms if not provided.
   * `[-gray, --gray]` -  Extracts the images in grayscale, used to generate test images

  ```
  python compare.py 'videos/testvideo.mp4' 'golden images/testvideo' -er 2000
  ```  
