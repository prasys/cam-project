import cv2
import time
import datetime
import os
import sys
import argparse
import keyboard
# from flask import Flask, render_template, Response
# # capture from webcam and save to file with timestamp
# app = Flask(__name__)

def main():
    #print app version and credits
    print("-----Cam v0.1------")
    print("-----(C) Pradeesh. Made with <3 for future padawans---------")
    print("-----May the Force be with you------")
    print("-----To Quit Press either Q or Control+C")



    parser = argparse.ArgumentParser(description='blah')
    parser.add_argument('-d', '--directory', default='.', help='directory to save images')
    parser.add_argument('-i', '--interval', default=1, type=int, help='interval between captures')
    parser.add_argument('-s', '--size', default=0, type=int, help='resize of image to capture')
    parser.add_argument('-c', '--camera', default=0, type=int, help='camera size')


    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print('Directory does not exist..Creating one :)')
        os.mkdir(args.directory)

        #sys.exit(1) 

    cam = cv2.VideoCapture(args.camera)
    if not cam.isOpened():
        print('Opps: Could not open Camera')
        sys.exit(1)
    
    try:
        while True:
            k = cv2.waitKey(1) & 0xFF 
            ret, frame = cam.read()
            if not ret:
                print('Error: could not read frame')
                sys.exit(1)


            if args.size > 0:
                frame = cv2.resize(frame, (args.size, args.size))

            filename = os.path.join(args.directory, datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f') + '.jpg')
            cv2.imwrite(filename, frame)
            print('Saved image to', filename)
            filename_static = os.path.join(args.directory, 'output.jpg')
            cv2.imwrite(filename_static, frame) #static file name that is needed 
            if keyboard.read_key() == 'Q' or keyboard.read_key() == 'q':
                cam.release()
                print("Exiting...")
                break
            time.sleep(args.interval)
    except KeyboardInterrupt:
        cam.release()
        print("Exiting...")
        #break the loop on escape key


if __name__ == '__main__':
    main()
