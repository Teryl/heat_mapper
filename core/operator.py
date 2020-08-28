import cv2

class Operator:
    """
    """

    def __init__(self):
        """
        """

        #
        self.sub = cv2.bgsegm.createBackgroundSubtractorMOG()

    def remove_background(self, frame):
        """
        """

        #
        filtered_frame = self.sub.apply(frame)

        return filtered_frame
