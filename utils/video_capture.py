import cv2


def capture_video_frames(num_frames=120):
    """
    Capture frames from webcam for a short duration.
    Frames are returned in memory and never stored.
    """

    cap = cv2.VideoCapture(0)

    frames = []

    count = 0

    while count < num_frames:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

        count += 1

    cap.release()
    cv2.destroyAllWindows()

    return frames