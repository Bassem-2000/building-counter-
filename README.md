results [here](https://drive.google.com/drive/folders/1B8mT2A4hc0FFTJkXq65FMWNiyOZepuZX?usp=sharing)
# Building Count from Drone Image

## Objective
The objective of this project is to detect and count the number of buildings in a provided drone image. The pipeline uses a pre-trained object detection model (YOLOv8) to identify buildings, annotate the image with bounding boxes, and return the total count of detected buildings.


GPU support (Optional but recommended for faster inference)

## Installation
- Clone the Repository:
    ```bash
    git clone https://github.com/yourusername/building-detection-pipeline.git
    ```
    ```bash
    cd building-detection-pipeline
    ```

- Create env and activate it:

    ```bash
    python -m venv .venv
    ```
    Activate on linux system

    ```bash
    source .venv/bin/activate  
    ```
    Activate on Windows System 
    ```bash
    source .venv\Scripts\activate  
    ```


- Install Dependencies:
    
    Install the necessary dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```
- Model Setup:

    Download the pre-trained models by runing this command.

    ```bash
    bash models/download_models.sh
    ```


## Project Structure

    ```
    .
    ├── config/
    │   └── config.yaml       # A yaml file contains the configs 
    ├── models/
    │   └── flkennedy.pt       # Pre-trained YOLOv8 model
    ├── output/
    │   └── annotated_image.jpg # Output image with bounding boxes (generated after running the script)
    ├── utils/
    │   └── config.py 
    │   └── image.py 
    │   └── model.py 
    ├── README.md
    ├── documentatio.pdf      # a documentation for this project
    ├── inference.py      # Main script to detect and count buildings
    └── requirements.txt       # List of dependencies
    ```


## Quick Start:

Place the drone image you want and run this command with the path of your image.

    ```bash
    inference.py --footprint <image.png>
    ```
## Expected Output:

The total count of detected buildings is printed in the console and also on the output image.
An annotated image with bounding boxes around the detected buildings is displayed in pop-up windows and saved to the output/ directory as annotated_image.jpg.

- Example
    Input: 
    
    A drone image provided as input (e.g., drone_image.jpg).
- Output:

    Annotated image with bounding boxes around detected buildings. Building count displayed in the console and a text with building count at the top left of the image.

## Code Explanation:

- load_image(): This function loads and preprocesses the input image for model inference.
- load_detection_model(): Loads the pre-trained YOLOv8 model with specified parameters such as confidence threshold and device (GPU or CPU).
- draw_predictions_on_image(): Draws bounding boxes and masks on the image for detected buildings.
- display_image_popup(): Displays the annotated image in a pop-up window using OpenCV.
- process_image(): The main function that handles the entire pipeline: image loading, model inference, post-processing, and output generation.

## Output Image Example

<div align="center">
    <img src="https://github.com/Bassem-2000/building-counter-/blob/main/images/output.png?raw=true?raw=true">
  </div>
