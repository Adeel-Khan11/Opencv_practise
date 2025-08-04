import cv2

def record_and_maybe_save():
    cap = cv2.VideoCapture(0)
    frames = []

    print("Recording started... Press 'q' to stop.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame!")
            break

        frames.append(frame)
        cv2.imshow("Webcam Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording stopped.")
            break

    cap.release()
    cv2.destroyAllWindows()

    
    choice = input("Do you want to save the video? (y/n): ").strip().lower()
    if choice == 'y':
        save_video(frames)
    else:
        print("Video was not saved.")

def save_video(frames):
    if not frames:
        print("No frames to save.")
        return

    height, width, _ = frames[0].shape
    codecs=cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("output_video.avi",codecs , 20, (width, height))

    for frame in frames:
        out.write(frame)

    out.release()
    print("Video saved as 'output_video.avi'")

if __name__ == "__main__":
    record_and_maybe_save()
