import cv2


class Stream:
    """A Stream class enables an user from loading a file and streaming it.

    """

    def __init__(self, source):
        """Initialization method.

        Args:
            source (string): File that should be loaded as a video.

        """

        # Creating a property for the VideoCapture from `source`
        self.video = cv2.VideoCapture(source)

    def read(self):
        """Reads a new frame.

        Returns:
            Whether frame is valid and the frame that has been read itself.

        """
        # Reads the next frame
        self.ret, self.frame = self.video.read()

        return self.ret, self.frame

    def full_length(self):
        """Checks if video has already displayed its full length.

        Returns:
            Whether video has already displayed its full length.

        """

        # Gathers the number of current frame
        current_frame = self.video.get(cv2.CAP_PROP_POS_FRAMES)
        
        # Gathers the amount of frames
        total_frames = self.video.get(cv2.CAP_PROP_FRAME_COUNT)

        # Checks if current frame equals to the amount of total frames
        if current_frame == total_frames:
            # If yes, return as True
            return True

        # If not, return as False
        return False

    def stop(self):
        """Stops the capture and releases the device.

        """

        # Releases the capture device
        self.video.release()
