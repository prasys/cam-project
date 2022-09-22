import cv2
import time
import datetime
import os
import sys
import argparse
from flask import Flask, render_template, Response
# capture from webcam and save to file with timestamp
app = Flask(__name__)

def main():

    parser = argparse.ArgumentParser(description='blah')
    parser.add_argument('-d', '--directory', default='.', help='directory to save images')
    parser.add_argument('-n', '--number', default=1, type=int, help='number of images to capture')
    parser.add_argument('-i', '--interval', default=1, type=int, help='interval between captures')
    parser.add_argument('-s', '--size', default=0, type=int, help='size of image to capture')
    parser.add_argument('-c', '--camera', default=0, type=int, help='camera size')
    parser.add_argument('-l', '--live', default=0, type=int, help='live video')


    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        # print('Error: directory does not exist')
        os.mkdir(args.directory)

        sys.exit(1)
        

    cam = cv2.VideoCapture(args.camera)
    if not cam.isOpened():
        print('Error: could not open camera')
        sys.exit(1)
    
    if args.live == 1:
        app.run(debug=False)

    for i in range(args.number):
        ret, frame = cam.read()
        if not ret:
            print('Error: could not read frame')
            sys.exit(1)
        # else:
        #     ret, buffer = cv2.imencode('.jpg', frame)
        #     frame = buffer.tobytes()
        #     yield (b'--frame\r\n'
        #            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

        if args.size > 0:
            frame = cv2.resize(frame, (args.size, args.size))

        filename = os.path.join(args.directory, datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f') + '.jpg')
        cv2.imwrite(filename, frame)
        print('Saved image to', filename)
        time.sleep(args.interval)

    cam.release()

# @app.route('/video_feed')
# def video_feed():
#     #Video streaming route. Put this in the src attribute of an img tag
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/')
# def index():
#     """Video streaming home page."""
#     return render_template('index.html')



if __name__ == '__main__':
    main()
