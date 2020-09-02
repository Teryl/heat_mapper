# Heat Mapper: An OpenCV-based Motion Detector

An image processing utility built upon OpenCV to generate motion heat maps from video-based sources.

*Note that this application is purely inspired by [intel-iot-devkit/motion-heatmap-cpp](https://github.com/intel-iot-devkit/motion-heatmap-cpp).*

---

## Installation

Install all the pre-needed requirements using:

```pip install -r requirements.txt```

---

## Getting Started

This repository is composed of three scripts that assist one in producing a heat map of a motion-based video.

### Displaying Video

The first step is to test whether the video is displaying correctly. Use the following script and pass a source file that contains a video as its argument:

```python video_displaying.py -h```

*Note that `-h` invokes the script helper, which assists users in employing the appropriate parameters.*

### Heat Mapping

Afteward, it is possible to construct a heat map based on the video's motion. Essentially, the algorithm removes the static background and sequentially accumulates the motion throughout the frames. At the end of the process, the resulting images will composed the motion-based masks and the individual frames.

```python heat_mapping.py -h```

*The --write flag defines whether the video will be displayed as an inline screen or saved to disk.*

## Rendering Video

Finally, with every frame outputted as an image, it is possible to reconstruct them back to a video. Use the following script to achieve such a purpose:

```python video_rendering.py -h```

*Note that the video is configured to render as an `.mp4`. If necessary, change the codec according to the desired extension.*

---

## Environment configuration

Note that sometimes, there is a need for additional implementation. If needed, from here, you will be the one to know all of its details.

### Ubuntu

No specific additional commands needed.

### Windows

No specific additional commands needed.

### MacOS

No specific additional commands needed.

---

## Support

We know that we do our best, but it is inevitable to acknowledge that we make mistakes. If you ever need to report a bug, report a problem, talk to us, please do so! We will be available at our bests at this repository or gustavo.rosa@unesp.br.

---
