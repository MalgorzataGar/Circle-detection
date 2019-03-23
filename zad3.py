

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    if ret is True:
        frame = cv2.medianBlur(frame, 5)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        output = frame.copy()
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)


        if circles is not None:

            circles = np.round(circles[0, :]).astype("int")

            for (x, y, r) in circles:

                cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)


            cv2.imshow("output", np.hstack([output]))

    else:
      continue
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()








