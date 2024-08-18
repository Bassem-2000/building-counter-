import logging
from sahi import AutoDetectionModel


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_detection_model(model_config):
    """Load the auto-detection model based on model configuration."""
    try:
        detection_model = AutoDetectionModel.from_pretrained(
            model_type=model_config['model_type'],
            model_path=model_config['model_path'],
            confidence_threshold=model_config['confidence_threshold'],
            device=model_config['device']
        )
        logging.info(f"Model {model_config['model_type']} loaded from {model_config['model_path']}")
        return detection_model
    except Exception as e:
        raise Exception(f"Error loading model: {str(e)}")