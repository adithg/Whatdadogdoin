import cv2

# initialize the video camera (use 0 for the default camera)
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('tradevid.mp4', fourcc, 30.0, (640, 480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Write the frame into the file 'output.mp4'
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Stop recording when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()