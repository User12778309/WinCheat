import cv2

print('''
       |-----------------------------------------|
       |    OPEN WEBCAM DEVICE ( 10 )             |
       |-----------------------------------------|
       
       Press Esc to quit
''')

cap = cv2.VideoCapture(0)

while True:

    success,frame = cap.read()
    if success == 0:
        print("Error")

    else:

        cv2.imshow("Webcam",frame)
        if cv2.waitKey(30) == 27:
            break

cap.release()
cv2.destroyAllWindows()