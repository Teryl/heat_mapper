import cv2

#
BG_SUB = cv2.bgsegm.createBackgroundSubtractorMOG()


def remove_background(frame):
    """
    """

    #
    frame = BG_SUB.apply(frame)

    return frame


def threshold(frame, threshold=2, max_value=2):
    """
    """

    #
    _, frame = cv2.threshold(frame, threshold, max_value, cv2.THRESH_BINARY)

    return frame
