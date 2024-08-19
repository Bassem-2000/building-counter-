results here https://drive.google.com/drive/folders/1B8mT2A4hc0FFTJkXq65FMWNiyOZepuZX?usp=sharing
# Project Title: Building Count from Drone Image

## Objective: Detect and count buildings in a provided drone image using a pre-trained YOLOv8 object detection model, returning the total count and an annotated image.

## Requirements: Python 3.x, OpenCV, Matplotlib, YOLOv8 Detection Library (e.g., from Ultralytics or another implementation), Pre-trained YOLOv8 Model (flkennedy.pt), GPU (Optional but recommended for faster inference).

## Installation:

Clone the repo: git clone https://github.com/yourusername/building-detection-pipeline.git && cd building-detection-pipeline
Install dependencies: pip install opencv-python-headless matplotlib yolov8-detection-library
Model Setup: Download the pre-trained YOLOv8 model (flkennedy.pt) and place it in the models/ directory.
Input Image: Place your drone image in the project directory or specify its path in the script.
## Project Structure:

README.md: Documentation.
building_count.py: Main script for building detection and counting.
models/flkennedy.pt: Pre-trained YOLOv8 model.
output/annotated_image.jpg: Generated output image with bounding boxes.
## Usage:
Run the script: python building_count.py.
The model will:

Load the drone image and the YOLOv8 model.
Perform detection and count the buildings.
Display and save the annotated image in the output/ folder.
## Parameters:

image_path: Path to the drone image (e.g., drone_image.jpg).
model_path: Path to the pre-trained YOLOv8 model (e.g., models/flkennedy.pt).
## Example Output:

Output Image: Annotated with bounding boxes around detected buildings, saved as annotated_image.jpg.
Console Output: Number of buildings detected: 15
## Code Overview:

load_image(): Loads and preprocesses the input image.
load_detection_model(): Loads the YOLOv8 model with specified parameters.
draw_predictions_on_image(): Annotates the image with bounding boxes and masks.
display_image_popup(): Displays the annotated image in a pop-up window.
process_image(): Handles the full pipeline from loading, detecting, to saving the annotated image.
## Notes:

Ensure the model weights (flkennedy.pt) are placed in the models/ directory.
Make sure the image path is correctly specified in the code.
