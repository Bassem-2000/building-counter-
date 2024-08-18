import logging
import yaml

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path):
    """Load configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: Configuration loaded from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        logging.info(f"Configuration loaded from {config_path}")
        return config
    except FileNotFoundError as fnf_error:
        logging.error(f"Configuration file not found: {fnf_error}")
        raise
    except yaml.YAMLError as yaml_error:
        logging.error(f"Error parsing YAML file: {yaml_error}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        raise
