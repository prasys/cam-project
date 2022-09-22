import cv2
import time
import datetime
import os
import sys
import argparse
# from flask import Flask, render_template, Response
# # capture from webcam and save to file with timestamp
# app = Flask(__name__)

def main():
    #print app version and credits
    print("-----Cam v0.1------")
    print("-----C) Pradeesh. Made with <3 for future padawans---------")
    print("-----May the Force be with you------")
    print("-----To Quit Press Escape")



    parser = argparse.ArgumentParser(description='blah')
    parser.add_argument('-d', '--directory', default='.', help='directory to save images')
    parser.add_argument('-n', '--number', default=1, type=int, help='number of images to capture')
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
    
    if args.live == 1:
        app.run(debug=False)

    while True:
        ret, frame = cam.read()
        if not ret:
            print('Error: could not read frame')
            sys.exit(1)
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

        if args.size > 0:
            frame = cv2.resize(frame, (args.size, args.size))

        filename = os.path.join(args.directory, datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f') + '.jpg')
        cv2.imwrite(filename, frame)
        print('Saved image to', filename)
        time.sleep(args.interval)
        #break loop on escape key
        if cv2.waitKey(1) == 27:
            cam.release()
            break

if __name__ == '__main__':
    main()
