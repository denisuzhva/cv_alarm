import numpy as np
from cv2 import cv2
import sound_processor as sp



def web_cam_params():
    """
    get webcam characteristics
    """
    cap = cv2.VideoCapture(0)
    print("Cap width:")
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("Cap height:")
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


if __name__ == '__main__':

    # Read initial frames
    cap = cv2.VideoCapture(0)
    cap_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    _, frame1 = cap.read()
    _, frame2 = cap.read()

    # Text paraneters
    text_string = 'ZHOPA'
    color = (255, 0, 0)
    font_face = cv2.FONT_HERSHEY_COMPLEX
    scale = 1
    thiccness = 2
    pos = (20, 40)

    while cap.isOpened():
        # Calculate difference
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        # Detect motion as high difference
        px_sum = np.sum(diff)
        print(px_sum)
        if px_sum > 4e6:
            sp.one_shot()
            cv2.putText(gray, text=text_string, 
                        org=pos,
                        fontFace=font_face,
                        fontScale=scale, 
                        color=color,
                        thickness=thiccness)

        # Display the resulting frame
        cv2.imshow('frame', gray)

        # Get new frame
        frame1 = frame2
        _, frame2 = cap.read()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


