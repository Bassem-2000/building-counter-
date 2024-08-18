import os
from time import time
import logging
import argparse
import cv2
from utils.image import load_image
from utils.image import save_image
from utils.image import get_building_count
from utils.image import display_image_popup
from utils.image import draw_predictions_on_image
from utils.config import load_config
from sahi.predict import get_sliced_prediction
from utils.model import load_detection_model

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_image(image_path, model_configs, config):
    """Process a single image with multiple models."""
    # Load image
    image = load_image(image_path)
    
    for model_config in model_configs:
        # Load detection model for each model configuration
        detection_model = load_detection_model(model_config)
        model_name =model_config['model_name']
        # Perform prediction
        start_time = time()
        result = get_sliced_prediction(
            image,
            detection_model,
            slice_height=config['slice_height'],
            slice_width=config['slice_width'],
            overlap_height_ratio=config['overlap_height_ratio'],
            overlap_width_ratio=config['overlap_width_ratio'],
            postprocess_class_agnostic=config['postprocess_class_agnostic']
        )
        logging.info(f"Prediction with model {model_config['model_type']} took {time() - start_time:.2f} seconds.")
        
        # Check for predictions
        if not result.object_prediction_list:
            logging.warning(f"No objects detected in the image with model {model_config['model_type']}.")
        else:
            # Get the building count
            building_count = get_building_count(result.object_prediction_list)
            logging.info(f"Number of buildings detected with model {model_config['model_type']}: {building_count}")
            
            # Draw predictions on the image
            image_with_predictions = draw_predictions_on_image(image.copy(), result.object_prediction_list)

            # Display the image in a pop-up window
            display_image_popup(image_with_predictions, window_name=f"{os.path.basename(image_path).split('.')[0]}-{model_name}")    
            
            # Save the processed image
            output_file_name = os.path.basename(image_path).replace('.', f"_{model_config['model_type']}.")
            output_path = os.path.join(config['output_dir'], f'{model_name}.{output_file_name.split(".")[-1]}')
            print(output_path)
            save_image(image_with_predictions, output_path)
    
    # Wait indefinitely until a key is pressed to close all windows
    while True:
        # Wait for a short period to handle GUI events
        if cv2.waitKey(1) & 0xFF == 27:  
            # ESC key to break out of loop
            break

    # Close all windows
    cv2.destroyAllWindows()


def main(image_path):
    # Load config
    config = load_config('config/config.yaml')

    # Get the list of model configurations
    model_configs = config['models']

    # Process image 
    process_image(image_path, model_configs, config)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Object Detection Script")
    parser.add_argument('--footprint', type=str, required=False, default='Untitled.jpg', help="Path to the footprintpath file.")
    args = parser.parse_args()
    
    main(args.footprint)