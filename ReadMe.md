<h1>Metadata Extractor and GeoLocator on Images</h1>
<h1>Description: </h1>
This project is an image viewer and metadata extractor application built using PyQt, a set of Python bindings for the Qt application framework. The application allows users to view geo-tagged images, navigate through them, and extract metadata information such as latitude and longitude.

<h1>Features</h1>
<h1>Real-Time Image Display:</h1>

View geo-tagged images in real-time as they are added to a specified directory.
Navigate through images using "Previous" and "Next" buttons.
Interrupt and resume the automatic flow of image display.


<h1>Metadata Extraction:</h1>

Click on any point in an image to extract metadata, including the latitude and longitude of the image's center.
Calculate the latitude and longitude of the pixel clicked by the user.
**Tech Stack**<br>
Python: Programming language used for application development.<br>
PyQt: Python bindings for the Qt framework, providing a rich set of tools for GUI development.<br>
Pillow (PIL): Python Imaging Library for image processing.<br>
OpenCV: Computer vision library for real-time image display.<br>
Watchdog: Python library for monitoring file system changes.



Certainly! Below is a simple template for a README file for your PyQt-based image viewer and metadata extractor project. Feel free to customize it based on your specific project details and requirements.

Image Viewer and Metadata Extractor
Description
This project is an image viewer and metadata extractor application built using PyQt, a set of Python bindings for the Qt application framework. The application allows users to view geo-tagged images, navigate through them, and extract metadata information such as latitude and longitude.

Features
Real-Time Image Display:

View geo-tagged images in real-time as they are added to a specified directory.
Navigate through images using "Previous" and "Next" buttons.
Interrupt and resume the automatic flow of image display.
Metadata Extraction:

Click on any point in an image to extract metadata, including the latitude and longitude of the image's center.
Calculate the latitude and longitude of the pixel clicked by the user.
Tech Stack
Python: Programming language used for application development.
PyQt: Python bindings for the Qt framework, providing a rich set of tools for GUI development.
Pillow (PIL): Python Imaging Library for image processing.
OpenCV: Computer vision library for real-time image display.
Watchdog: Python library for monitoring file system changes.
Installation
Clone the repository:
git clone https://github.com/your-username/image-viewer-metadata-extractor.git
cd image-viewer-metadata-extractor

Install dependencies:
pip install -r requirements.txt

Run the application:
python main.py
