from email.mime import image
import apriltag
import cv2

path = ''

print('[INFO] Loading image...')
image = cv2.imread(path, 0) # Load the image in grayscale format

print('[INFO] Detecting AprilTags...')
options = apriltag.DetectorOptions(families='tag36h11') # Define the detector's option
detector = apriltag.Detector(options)
results = detector.detect(image)
print(f'[INFO] {len(results)} Total AprilTags detected')

# Looping over the results
for r in results:
    # Extract the bounding box coordinates for 
    # the AprilTag and convert it to integers
    ptA, ptB, ptC, ptD = r.corners
    ptA = (int(ptA[0]), int(ptA[1]))
    ptB = (int(ptB[0]), int(ptB[1]))
    ptC = (int(ptC[0]), int(ptC[1]))
    ptD = (int(ptD[0]), int(ptD[1]))

    # Draw the bounding boxes
    cv2.line(image, ptA, ptB, (0, 255, 0), 2)
    cv2.line(image, ptB, ptC, (0, 255, 0), 2)
    cv2.line(image, ptC, ptD, (0, 255, 0), 2)
    cv2.line(image, ptD, ptA, (0, 255, 0), 2)

    # Draw the center coordinates of the AprilTag
    cX, cY = int(r.center[0]), int(r.center[1])
    cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1) 

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()