import cv2

# Constant that defines the background subtractor
BG_SUB = cv2.bgsegm.createBackgroundSubtractorMOG()


def remove_background(frame):
    """Removes background from a frame.

    Args:
        frame (np.array): Array representing the frame.

    Returns:
        Background-less frame.

    """

    # Subtracts the background from the frame
    frame = BG_SUB.apply(frame)

    return frame


def threshold(frame, threshold=2, max_value=2):
    """Applies a binary threshold to a frame.

    Args:
        frame (np.array): Array representing the frame.
        threshold (int): Threshold to be evaluated.
        max_value (int): Maximum value to be replaced if beyond threshold.

    Returns:
        Thresholded frame.

    """

    # Thresholds the frame
    _, frame = cv2.threshold(frame, threshold, max_value, cv2.THRESH_BINARY)

    return frame
