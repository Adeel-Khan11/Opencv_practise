import cv2

# Load cascades once
face_cascade = cv2.CascadeClassifier(
    r'C:\Users\khan\Desktop\cv2_practise\day 09\haarcascade_frontalface_default.xml'
)
eye_cascade = cv2.CascadeClassifier(
    r'C:\Users\khan\Desktop\cv2_practise\day 09\haarcascade_eye.xml'
)
smile_cascade = cv2.CascadeClassifier(
    r'C:\Users\khan\Desktop\cv2_practise\day 09\haarcascade_smile.xml'
)

def detect_face_and_eyes():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (fx, fy, fw, fh) in faces:
            
            cv2.rectangle(frame, (fx, fy), (fx+fw, fy+fh), (0, 255, 0), 2)

       
            face_gray = gray[fy:fy+fh, fx:fx+fw]
            face_color = frame[fy:fy+fh, fx:fx+fw]

            eyes = eye_cascade.detectMultiScale(face_gray, 1.1, 5)
            for (ex, ey, ew, eh) in eyes:
              
                cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

      
            if len(eyes) > 0:
                cv2.putText(frame,
                            "Eyes Detected",
                            (fx, fy - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 255, 0),
                            2)

        cv2.imshow('Face & Eye Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def detect_faces_only():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Face Detection Only', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def detect_face_eye_smile():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (fx, fy, fw, fh) in faces:
            cv2.rectangle(frame, (fx, fy), (fx+fw, fy+fh), (0, 255, 0), 2)
            face_gray = gray[fy:fy+fh, fx:fx+fw]
            face_color = frame[fy:fy+fh, fx:fx+fw]

            
            eyes = eye_cascade.detectMultiScale(face_gray, 1.1, 5)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

            
            smiles = smile_cascade.detectMultiScale(face_gray, scaleFactor=1.7, minNeighbors=22)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(face_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

            
            label = []
            if len(eyes) > 0:
                label.append('Eyes')
            if len(smiles) > 0:
                label.append('Smile')
            if label:
                text = ' & '.join(label) + ' Detected'
                cv2.putText(frame,
                            text,
                            (fx, fy - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 255, 255),
                            2)

        cv2.imshow('Face, Eye & Smile Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    while True:
        print('''
1: Face detection only
2: Face + Eye detection
3: Face + Eye + Smile detection
4: Exit
''')
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            detect_faces_only()
        elif choice == '2':
            detect_face_and_eyes()
        elif choice == '3':
            detect_face_eye_smile()
        elif choice == '4':
            print("Good bye!")
            break
        else:
            print("Invalid choice, try again.")