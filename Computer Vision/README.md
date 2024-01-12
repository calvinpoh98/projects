
# Floor Plan Segmentation Using OpenCV and Docker

This project demonstrates the use of OpenCV for image segmentation on floor plans. The primary goal is to identify and separate different rooms within a floor plan image, utilizing various computer vision techniques.

## Features

- **Preprocessing**: Converts images to grayscale to simplify the segmentation process.
- **Thresholding**: Applies binary thresholding to isolate the structures within the floor plans.
- **Morphological Operations**: Uses morphological operations to enhance the quality of the image and highlight the contours.
- **Watershed Algorithm**: Implements the watershed algorithm for precise segmentation of adjoining rooms.
- **Docker Integration**: Packages the application within a Docker container for easy deployment and scalability.

## Usage

To run the segmentation script inside a Docker container, follow these steps:

1. **Build the Docker Image**:
   ```sh
   docker build -t floorplan-segmentation .
   ```

2. **Run the Container**:
   ```sh
   docker run -p 4000:80 floorplan-segmentation
   ```

The script processes the input floor plan image and outputs a segmented image, where each room is marked with a unique color.

## Dockerfile Explanation

The provided Dockerfile sets up a Python environment with all the necessary dependencies to run the OpenCV script. It copies the source code into the container, installs the dependencies from `requirements.txt`, and specifies the command to run the script.

## Further Improvements

Future updates to this project will explore the use of advanced image segmentation models such as U-Net, which are particularly adept at handling complex segmentation tasks. This deep learning approach can significantly enhance the precision of room segmentation in floor plans, especially in cases where traditional computer vision techniques may fall short.
