import cv2
import logging
import numpy as np
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_image(image_path):
    """Load and preprocess the image."""
    try:
        image = cv2.imread(image_path)#[1000:2000,1000:2000]
        if image is None:
            raise FileNotFoundError(f"Image at {image_path} not found.")
        logging.info(f"Loaded image: {image_path}")
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception as e:
        raise Exception(f"Error loading image: {str(e)}")

def get_building_count(predictions, score_threshold=0.4):
    """
    Count the number of buildings (objects) detected that meet the score threshold.
    
    Args:
        predictions (list): List of object predictions.
        score_threshold (float): Minimum score for a detection to be counted.
        
    Returns:
        int: Count of buildings detected.
    """
    building_count = 0
    for prediction in predictions:
        if prediction.score.value >= score_threshold:
            building_count += 1
    return building_count
def draw_predictions_on_image(image, predictions, score_threshold=0.4):
    """
    Draw bounding boxes, masks, and building count on the image.
    
    Args:
        image (np.array): The image on which to draw the predictions.
        predictions (list): List of object predictions.
        score_threshold (float): Minimum score for a detection to be drawn.
        
    Returns:
        np.array: The image with bounding boxes, masks, and building count drawn.
    """
    building_count = 0

    for prediction in predictions:
        if prediction.score.value < score_threshold:
            continue
        
        # Draw bounding box
        cv2.rectangle(
            image,
            (prediction.bbox.minx, prediction.bbox.miny),
            (prediction.bbox.maxx, prediction.bbox.maxy),
            (0, 0, 0), 2
        )

        # Apply mask if available
        if hasattr(prediction, 'mask') and prediction.mask is not None:
            mask = prediction.mask.bool_mask
            if mask.dtype != bool:
                mask = mask.astype(bool)
            # Highlight the mask on the image
            image[mask] = (image[mask] * 0.5 + np.array([0, 255, 255]) * 0.5).astype(np.uint8)
        
        building_count += 1

    # Add text annotation for building count
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (0, 255, 0)  # Green color for the text
    line_type = 2
    text = f"Buildings: {building_count}"
    position = (10, 30)  # Position of the text in the image
    cv2.putText(image, text, position, font, font_scale, font_color, line_type)

    return image

def display_image_popup(image, window_name="Image"):
    """Display the image in a pop-up window using OpenCV."""
    
    # Convert the image back to BGR for OpenCV display
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Show the image in a window
    cv2.imshow(window_name, image_bgr)
    
    # Create a named window, this allows the window to remain open independently
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    
    # Wait indefinitely until a key is pressed
    cv2.waitKey(1)

def save_image(image, output_path):
    """Save the processed image to a file."""
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    logging.info(f"Processed image saved to {output_path}")
