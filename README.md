# Square your images

This is a Python script that will crop or resize your .png or .jpg files into a square. Duplicate results are overwritten. I made this short program because I got lazy cropping each image for my personal website.

## Features

- **Crop**: Crop images to a square, focusing on the center of the image and based on the larger of the width or height.
- **Resize**: Resize images to a square, using the largest side of the image to determine the new size, thus maintaining the aspect ratio.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Ensure Python 3.x is installed

2. Install the Pillow library using pip:

   ```sh
   pip install Pillow
   ```

## Usage

1. cd into directory with main.py
2. change the "action" variable depending on your preference
3. upload images into the /input folder
4. run program using 'python main.py'
5. results are uploaded into the /results folder
