import cv2

face_cascade = cv2.CascadeClassifier("c:\Program haarcascade_frontalface_default.xml")
video_cap=cv2.VideoCapture(0)
while True:
    ret, video_data = video_cap.read()
    col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(col, 1.1)

    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()
