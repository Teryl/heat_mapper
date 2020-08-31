import argparse
import os
import re

import cv2
from tqdm import tqdm


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Renders a collection of images into a video.')

    parser.add_argument('source', help='Identifier to folder that should be rendered as a video.', type=str)

    parser.add_argument('-output', help='Identifier to output video.', type=str, default='output.mp4')

    parser.add_argument('-fps', help='Number of frames per second.', type=float, default=30.0)

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments
    args = get_arguments()

    # Gathers variables from arguments
    source = args.source
    output = args.output
    fps = args.fps

    # Gathers a file list from the selected folder
    source_folder = [f for f in os.listdir(source) if f.endswith('.jpg')]

    # Sorts the folder incrementally
    source_folder.sort(key=lambda f: int(re.sub('\D', '', f)))

    # Gathers the height and width of input files
    height, width, _ = cv2.imread(os.path.join(source, source_folder[0])).shape

    # Creates the .mp4 codec
    codec = cv2.VideoWriter_fourcc(*'mp4v')

    # Creates the video writer
    out = cv2.VideoWriter(output, codec, fps, (width, height))

    print(f'Rendering frames to: {output}')

    # Iterates over amount of possible frames
    for source_file in tqdm(source_folder):
        # Loads the frame
        frame = cv2.imread(os.path.join(source, source_file))

        # Writes the frame
        out.write(frame)

    # Releases the video writer
    out.release()

    print('Video rendered.')
