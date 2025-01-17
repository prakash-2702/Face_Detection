# python face_detection.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.7, help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

print("[ALERT] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# initialize the video stream and allow the cammera sensor to warmup
print("[ALERT] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
 
	(h, w) = frame.shape[:2]
	# Blob stands for Binary Large Object and refers to the connected pixel in the binary image.
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))
 
	# pass the blob through the network and obtain the detections and predictions
	net.setInput(blob)
	detections = net.forward()

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability)
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the confidence is greater than the minimum confidence
		if confidence < args["confidence"]:
			continue

		# compute the (x, y)-coordinates of the bounding box for the object
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(start_x, start_y, end_x, end_y) = box.astype("int")
 
		# draw the bounding box of the face along with the associated probability
		put_text = "{:.2f}%".format(confidence * 100)
		cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)
		cv2.putText(frame, put_text, (start_x, start_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# press a to end
	if key == ord("a"):
		break

cv2.destroyAllWindows()
vs.stop()