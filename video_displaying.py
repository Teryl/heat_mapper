import argparse

import cv2
from tqdm import tqdm

from core.stream import Stream


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Loads a video and displays it.')

    parser.add_argument('source', help='Identifier to file that should be loaded as a video.', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments
    args = get_arguments()

    # Gathers variables from arguments
    source = args.source

    # Starts an instance from the `Stream` class
    v = Stream(source)

    # Iterates over amount of possible frames
    for _ in tqdm(range(v.total_frames)):
        # Reads a new frame
        valid, frame = v.read()

        # Checks if frame is valid
        if valid:
            # Shows the frame
            cv2.imshow('video', frame)

        # If the `q` key is inputted, breaks the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stops the instance
    v.stop()

    # Destroy all windows for cleaning up memory
    cv2.destroyAllWindows()
