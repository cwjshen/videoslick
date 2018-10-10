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
