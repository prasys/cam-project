import cv2
import time
import datetime
import os
import sys
import argparse
# capture from webcam and save to file with timestamp
def main():


    parser = argparse.ArgumentParser(description='blah')
    parser.add_argument('-d', '--directory', default='.', help='directory to save images')
    parser.add_argument('-n', '--number', default=1, type=int, help='number of images to capture')
    parser.add_argument('-i', '--interval', default=1, type=int, help='interval between captures')
    parser.add_argument('-s', '--size', default=0, type=int, help='size of image to capture')
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print('Error: directory does not exist')
        sys.exit(1)

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print('Error: could not open camera')
        sys.exit(1)

    for i in range(args.number):
        ret, frame = cam.read()
        if not ret:
            print('Error: could not read frame')
            sys.exit(1)

        if args.size > 0:
            frame = cv2.resize(frame, (args.size, args.size))

        filename = os.path.join(args.directory, datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f') + '.jpg')
        cv2.imwrite(filename, frame)
        print('Saved image to', filename)
        time.sleep(args.interval)

    cam.release()

    if __name__ == '__main__':
        main()
