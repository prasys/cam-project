# Cam Project
A simple python script that captures images using OpenCV and stores it to a folder. The application also contains features such as the ability to 
specify a camera, the path to where to save the file and the interval given (in seconds)


## Installation

### Requirements

You need [Python 3.8](https://www.python.org/downloads/release/python-380/) and a Webcam that is compatible with your operating system. 

This script has been tested on MacOS 10.14 and also on Windows 11. It is known to work on any other operating system where python is compatible such as Linux, Windows and MacOS


### Installation Instructions 

Instructions for installing, for example command of package manager like

    git clone https://github.com/prasys/cam-project.git
    cd cam-project
    pip3 install -r requirements.txt

This will basically clone the repo and install all the dependencies which are required with `pip` 

## Usage

To run this program, simply execute the following 

    python3 cam.py

By default the application uses the default web-camera and stores the image every second to the current directory. It uses the camera's default resolution (i.e, 480p or 720p)

Suppose, if we want to to store our files in Google Drive in a folder called cam and to take pictures every 60 seconds, we can do the following

    python3 cam.py -d /Volumes/Google Drive/My \Drive/cam -i 60

Alternatively, if we want to enlarge the image (enlarge it by 50%) and use a different webcam (i.e, if you have two cameras such as in Microsoft Surface ) you may use the following, where it will use the other web camera (i.e, front camera in Microsoft Surface) and resizes the image by 50%. 

    python3 cam.py -c 1 -s 50

For more examples on how to use this commands, you may execute the following command 

    python3 cam.py -?
    
    
## Support

For any question on the usage of this software or if you found a problem with the software, please [create an issue](https://github.com/prasys/cam-project/issuess) on GitHub.


## License
Licensed under the [GNU General Public License v3.0 or later](LICENSE).

