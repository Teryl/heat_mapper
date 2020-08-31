import argparse

import cv2
from tqdm import tqdm

import utils.processing as p
from core.stream import Stream


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Loads a video and builds its heat map.')

    parser.add_argument('source', help='Identifier to file that should be loaded as a video.', type=str)

    parser.add_argument('--write', help='Writes heat map to disk.', action='store_true')

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments
    args = get_arguments()

    # Gathers variables from arguments
    source = args.source
    write = args.write

    # Starts an instance from the `Stream` class
    v = Stream(source)

    # Iterates over amount of possible frames
    for i in tqdm(range(v.total_frames)):
        # Reads a new frame
        valid, frame = v.read()

        # Checks if frame is valid
        if valid:
            # Creates a masked frame
            v.masked_frame = cv2.add(v.masked_frame, p.threshold(p.remove_background(frame)))

            # Colorizes the masked frame
            v.color_masked_frame = p.colorize(v.masked_frame)

            # Post-processed frame will be a weighted frame between current frame and colorized mask
            v.frame = cv2.addWeighted(frame, 0.5, v.color_masked_frame, 0.5, 0)

            # Checks if post-processed frame should be written to disk
            if write:
                # Outputs post-processed frame to disk
                v.output_frame(i+1)
            else:
                # Shows the post-processed frame
                cv2.imshow('video', v.frame)

        # If the `q` key is inputted, breaks the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stops the instance
    v.stop()

    # Outputs the masks as images
    v.output_masks()

    # Destroys all windows for cleaning up memory
    cv2.destroyAllWindows()
