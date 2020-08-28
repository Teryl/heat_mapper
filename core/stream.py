import cv2

# Constant that defines whether outputs will be saved
FOLDER = 'outputs/'


class Stream:
    """A Stream class enables an user from loading a file and streaming it.

    """

    def __init__(self, source):
        """Initialization method.

        Args:
            source (string): File that should be loaded as a video.

        """

        print(f'Initializing video from: {source}')

        # Creating a property for the VideoCapture from `source`
        self.video = cv2.VideoCapture(source)

        # Reads and saves the initial frame as a property
        _, self.initial_frame = self.video.read()

    @property
    def current_frame(self):
        """Gathers the number of current frame.

        """

        return int(self.video.get(cv2.CAP_PROP_POS_FRAMES))

    @property
    def total_frames(self):
        """Gathers the amount of total frames.

        """

        return int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

    def read(self):
        """Reads a new frame.

        Returns:
            Whether frame is valid and the frame that has been read itself.

        """

        # Reads the next frame
        ret, frame = self.video.read()

        return ret, frame

    def full_length(self):
        """Checks if video has already displayed its full length.

        Returns:
            Whether video has already displayed its full length.

        """

        # Checks if current frame equals to the amount of total frames
        if self.current_frame == self.total_frames:
            # If yes, return as True
            return True

        # If not, return as False
        return False

    def stop(self):
        """Stops the capture and releases the device.

        """

        print('Stopping video ...')

        # Releases the capture device
        self.video.release()

        print('Video stopped.')

    def output_images(self):
        """Outputs class properties as images.

        """

        print(f'Outputting images to: {FOLDER}')

        #
        cv2.imwrite(FOLDER + 'initial_frame.jpg', self.initial_frame)

        print('Images saved.')
