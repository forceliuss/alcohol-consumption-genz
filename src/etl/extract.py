import os
import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
DATA_URL = "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Alcohol%20consumption/Alcohol%20consumption.csv"
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'raw')

def download_data(url: str, output_dir: str):
    """
    Downloads data from the specified URL and saves it to the output directory.
    """
    try:
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y-%m-%d")
        filename = f"alcohol_consumption_{timestamp}.csv"
        file_path = os.path.join(output_dir, filename)
        
        logger.info(f"Starting download from {url}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        with open(file_path, 'wb') as f:
            f.write(response.content)
            
        logger.info(f"Successfully downloaded data to {file_path}")
        return file_path
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to download data: {e}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    try:
        download_data(DATA_URL, RAW_DATA_DIR)
    except Exception as e:
        logger.critical("Extraction process failed.")
        exit(1)
