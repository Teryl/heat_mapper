import argparse

import cv2

from utils.stream import Stream


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Loads a video and builds its heat map.')

    parser.add_argument('source', help='Identifier to file that should be loaded as a video.', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments
    args = get_arguments()

    # Gathering variables from arguments
    source = args.source

    # Starts an instance from the `Stream` class
    v = Stream(source)

    # While the loop is True
    while True:
        # Reads a new frame
        valid, frame = v.read()

        # Checks if frame is valid
        if valid:
            # Shows the frame using openCV
            cv2.imshow('video', frame)

        # Checks if video has already displayed its full length
        if v.full_length():
            break

        # If the `q` key is inputted, breaks the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stops the instance
    v.stop()
            
    # Destroy all windows for cleaning up memory
    cv2.destroyAllWindows()
