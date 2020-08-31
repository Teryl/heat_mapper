import os

import cv2
import numpy as np

# Constant that defines whether outputs will be saved
FOLDER = 'outputs/'
FRAMES_FOLDER = FOLDER + 'frames/'


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

        # Gathers the shape of the initial frame
        (height, width, n_channels) = self.initial_frame.shape

        # Masked frame
        self.masked_frame = np.zeros((height, width), np.uint8)

        # Colorized masked frame
        self.color_masked_frame = np.zeros((height, width), np.uint8)

        # Post-processed frame
        self.frame = np.zeros((height, width), np.uint8)

        # Checks if `frames` folder exists
        if not os.path.exists(FRAMES_FOLDER):
            # If not, creates the folder
            os.makedirs(FRAMES_FOLDER)

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

    def output_frame(self, index):
        """Outputs post-processed frame as an image.

        Args:
            index (int): Index of frame to be saved.

        """

        # Post-processed frame
        cv2.imwrite(FRAMES_FOLDER + f'frame_{index}.jpg', self.frame)

    def output_masks(self):
        """Outputs masks as images.

        """

        # Initial frame
        cv2.imwrite(FOLDER + 'initial_frame.jpg', self.initial_frame)

        # Masked frame
        cv2.imwrite(FOLDER + 'masked_frame.jpg', self.masked_frame)

        # Color masked frame
        cv2.imwrite(FOLDER + 'color_masked_frame.jpg', self.color_masked_frame)
